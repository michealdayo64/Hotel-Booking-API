from django.db import models
from hotels.models import Hotel
# Create your models here.

class RoomType(models.Model):
    room_type = models.CharField(max_length = 20)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.room_type

"""class RoomImage(models.Model):
    room_image = models.ImageField(upload_to = 'room', blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.room_image"""

class Room(models.Model):
    room_name = models.CharField(max_length = 20, null = True, blank = True)
    slug = models.SlugField()
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, null = True, blank = True, related_name = 'hotel')
    room_types =  models.ForeignKey(RoomType, on_delete = models.CASCADE, null = True, blank = True)
    room_status = models.BooleanField(default = True)
    price = models.FloatField(default = 0.0, blank = True, null = True)
    image1 = models.ImageField(upload_to = 'room', blank = True, null = True)
    image2 = models.ImageField(upload_to = 'room', blank = True, null = True)
    image3 = models.ImageField(upload_to = 'room', blank = True, null = True)
    image4 = models.ImageField(upload_to = 'room', blank = True, null = True)
    image5 = models.ImageField(upload_to = 'room', blank = True, null = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.room_name} of {self.room_types.room_type}"
    


