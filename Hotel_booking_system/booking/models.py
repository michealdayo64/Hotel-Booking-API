from django.db import models
from django.contrib.auth.models import User
from hotels.models import Hotel
from rooms.models import Room
from datetime import datetime
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_celery_beat.models import PeriodicTask, CrontabSchedule
import json
# Create your models here.


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'user')
    room = models.ForeignKey(Room, on_delete = models.CASCADE, related_name = 'room')
    book_date_from = models.DateTimeField()
    book_date_to = models.DateTimeField()
    ref_code = models.CharField(max_length=100, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True, related_name = 'payment')
    payment_status = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.username} booked {self.room.room_name}"

    @property
    def roomHasExpire(self):
        return datetime.datetime.now() >= self.book_date_to

class CheckInAndOut(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True, blank = False)
    booking = models.ForeignKey(Booking, on_delete = models.CASCADE, null = True, blank = False)
    checked = models.BooleanField(default = False)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)


class Payment(models.Model):
    charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender = Booking)
def expiredBooking(sender, instance, created, **kwargs):
    if created:
        schedule, created = CrontabSchedule.objects.get_or_create(hour = instance.book_date_to.hour, minute = instance.book_date_to.minute, day_of_month = instance.book_date_to.day, month_of_year = instance.book_date_to.month)
        task = PeriodicTask.objects.create(crontab = schedule, name = "schedule-id-" + str(instance.id), task = "booking.tasks.schedule_booking", args = json.dumps((instance.id, )))
 
