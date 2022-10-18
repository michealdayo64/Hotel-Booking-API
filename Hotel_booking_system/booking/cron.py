from .models import Booking
from django.utils import timezone

def my_cron_job():
    pass


def userBookingApi(request):
    user = request.user
    if user.is_authenticated:
        user_book = Booking.objects.get(user = user)
        if user_book.book_date_to <= timezone.now():
            user_book.payment_status = False
            user_book.save()
        