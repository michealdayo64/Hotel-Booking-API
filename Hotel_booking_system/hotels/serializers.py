from rest_framework import serializers
from .models import Facility, Address, Hotel
#from rooms.models import Room


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:

        model = Facility
        fields = (
            'pk',
            'facility',
        )

class AddressSerializer(serializers.ModelSerializer):
    class Meta:

        model = Address
        fields = (
            'pk',
            'city',
            'pinCode',
            'state',
            'streetNo',
            'landmark',

        )

class HotelSerializer(serializers.HyperlinkedModelSerializer):
    addrees = AddressSerializer(many = False, read_only = True)
    facilities = FacilitySerializer(many = True)


    class Meta:
    
        model = Hotel
        fields = (
            'pk',
            'hotel_name',
            'hotel_image',
            'addrees',
            'facilities',
            #'hotel'
        )