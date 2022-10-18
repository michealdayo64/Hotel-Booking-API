from django.urls import path
from booking import views


app_name = 'booking'

urlpatterns = [
    path('book_room_api/<id>/', views.book_room_api, name = 'book_room_api'),
    path('user_booking/', views.userBookingApi, name = 'user_booking'),
    path('booking_payment/', views.bookPayment, name = 'booking_payment'),
    #path('test/', views.test, name = 'test')
]