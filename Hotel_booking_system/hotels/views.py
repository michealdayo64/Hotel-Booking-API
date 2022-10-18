from django.shortcuts import render
from .serializers import FacilitySerializer, AddressSerializer, HotelSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Facility, Address, Hotel
from rooms.models import Room
from rooms.serializers import RoomSerializer
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone

# Create your views here.

#print(timezone.now())

#----------------------------API SECTION-------------------------

# FETCH HOTEL FACILITY
@api_view(['GET',])
@permission_classes((AllowAny,))
def facility_list_api(request):
    facilities = Facility.objects.all()
    facility = FacilitySerializer(facilities, many = True)
    if facility:
        data = {
            'msg': facility.data
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            'msg': "Error in fetching data"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)


# FETCH ADDRESS OF HOTEL
@api_view(['GET',])
@permission_classes((AllowAny,))
def address_list_api(request):
    addrees_list = Address.objects.all()
    address = AddressSerializer(addrees_list, many = True)
    if address:
        data = {
            'msg': address.data
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            'msg': "Error in fetching data"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)        

# FETCH HOTEL
@api_view(['GET',])
@permission_classes((AllowAny,))
def hotel_list_api(request):
    hotel_list = Hotel.objects.all().order_by('-created')[:3]
    hotel = HotelSerializer(hotel_list, many = True, context={'request': request})
    if hotel:
        data = {
            'msg': hotel.data
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            'msg': "Error in fetching data"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)  


# GET HOTEL ID
@api_view(['GET',])
@permission_classes((AllowAny,))
def hotel_id_api(request, id = None):
    if id:
        hotelId = Hotel.objects.get(id = id)
        print(hotelId)
        room = Room.objects.filter(hotel = hotelId)
        print(room)
        hot = RoomSerializer(many = True, instance = room)
        if hot:
            data = {
                'msg': hot.data
            }
            return Response(data = data, status = status.HTTP_200_OK)
        else:
            data = {
                'msg': "Error in fetching data"
            }
            return Response(data = data, status = status.HTTP_400_BAD_REQUEST)
    else:
        hot_room = Room.objects.all()
        hotRoom = RoomSerializer(hot_room, many = True)
        if hotRoom:
            data = {
                'msg': hotRoom.data
            }
            return Response(data = data, status = status.HTTP_200_OK)
        else:
            data = {
                'msg': "Error in fetching data"
            }
            return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

