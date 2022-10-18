from django.shortcuts import render, HttpResponse
from django.utils import timezone
from .serializers import BookingSerializer, PaymentSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Payment, Booking
from rooms.models import Room
from rest_framework import status
from rest_framework.response import Response
import time
from threading import Thread
import datetime
import random
import string
# Create your views here.

#Celery Imports
#from .tasks import test_func


def create_ref_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=16))


#----------------------------API SECTION-------------------------#


'''def test(request):
    test_func.delay()
    return HttpResponse("Done")'''


# Book a room
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def book_room_api(request, id):
    room_id = Room.objects.get(pk = id)
    user = request.user
    if request.method == 'POST':
        dateFrom = request.data.get("date_from")
        dataTo = request.data.get("date_to")
        if user.is_authenticated:
            booking = Booking(
                user = user,
                room = room_id,
                book_date_from = dateFrom,
                book_date_to = dataTo,
                ref_code = create_ref_code(),
                payment_status = True,
            )
            booking.save()
            room_id.room_status = False
            room_id.save()
            data = {
                "msg": f"{room_id.room_name} Booked Successfully"
            }
            return Response(data = data, status = status.HTTP_200_OK)
        else:
            data = {
                "msg": "User is not authenticated"
            }
            return Response(data = data, status = status.HTTP_400_BAD_REQUEST)


# User Book List
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def userBookingApi(request):
    user = request.user
    if user.is_authenticated:
        user_book = Booking.objects.get(user = user)
        user_book_serializer = BookingSerializer(user_book, many = False)
        data = {
            "msg": user_book_serializer.data
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            "msg": "Your need to be authenticated"
        }
        return Response(data = data, status = status.HTTP_200_OK)


@api_view(['GET', 'POST', ])
@permission_classes((IsAuthenticated,))
def bookPayment(request):
    user = request.user
    get_book = Booking.objects.get(user = user)
    #amount = request.data.get("amount")
    
    if user.is_authenticated:
        pay = Payment(charge_id = create_ref_code(), user = user, amount = get_book.room.price)
        pay.save()
        get_book.payment_status = True
        get_book.payment = pay
        get_book.save()
        Thread(target = expireBooking(user))
        data = {
            "Payed": f"{user.username} Payment made succesfully"
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            "Error": 'User not authenticated'
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

