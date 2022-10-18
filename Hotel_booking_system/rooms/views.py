from django.shortcuts import render
from .serializers import RoomTypeSerializer, RoomSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Room, RoomType
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

#----------------------------API SECTION-------------------------#

# FETCH ROOMS
@api_view(['GET',])
@permission_classes((AllowAny,))
def room_list_api(request):
    room_list = Room.objects.all().order_by('-created')[:3]
    rooms = RoomSerializer(room_list, many = True, context={'request': request})
    if rooms:
        data = {
            'msg': rooms.data
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            'msg': "Something is wrong"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)



# FETCH ROOMTYPE
@api_view(['GET',])
@permission_classes((AllowAny,))
def roomtype_list_api(request):
    roomtype_list = RoomType.objects.all()
    roomtype = RoomTypeSerializer(roomtype_list, many = True, context={'request': request})
    if roomtype:
        data = {
            "msg": roomtype.data
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            "msg": "Something is wrong"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)