from rest_framework import serializers
from .models import RoomType, Room
from hotels.serializers import HotelSerializer

class RoomTypeSerializer(serializers.ModelSerializer):
    class Meta:

        model = RoomType
        fields = (
            'pk',
            'room_type',
            'created',
            'updated',
        )


class RoomSerializer(serializers.ModelSerializer):
    hotel = HotelSerializer(many = False)
    room_types = RoomTypeSerializer(many = False)
    class Meta:

        model = Room
        fields = (
            'pk',
            'room_name',
            'room_types',
            'hotel',
            'room_status',
            'price',
            'image1',
            'image2',
            'image3',
            'image4',
            'image5',
            'created',
            'updated',
        )