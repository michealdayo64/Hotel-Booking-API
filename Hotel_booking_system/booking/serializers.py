from rest_framework import serializers
from .models import Booking, Payment
#from account.serializers import User
from hotels.serializers import HotelSerializer
from rooms.serializers import RoomSerializer




class PaymentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'user.username')
    class Meta:

        model = Payment
        fields = (
            'pk',
            'charge_id',
            'amount',
            'owner',
            'timestamp',
        )

class BookingSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'user.username')
    payment = PaymentSerializer(many = False)
    #hotel = HotelSerializer(many = False)
    room = RoomSerializer(many = False)

    class Meta:

        model = Booking
        fields = (
            'pk',
            'owner',
            'room',
            'book_date_from',
            'book_date_to',
            'payment',
            'payment_status',
            'created',
            'updated',

        )