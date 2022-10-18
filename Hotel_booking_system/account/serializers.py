from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth.models import User



class UserSerializer(serializers.ModelSerializer):
    #products = OrderItemSerializer(many = True, read_only = True)
    #user_profile = UserInfoSerializer(read_only = True)
    #user = Token.objects.all()
    class Meta:
        #model = UserInfo
        model = User
        fields = (
            'pk',
            'username',
            'email',
            'password',
            #'user_profile',
            #'auth_token'
        )
        extra_kwargs = {'password': {'write_only': True}}


class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(many = False)
    class Meta:
        model = UserInfo
        fields = (
            'pk',
            'user',
            'phone_no', 
            'address',
            #'slug',
        )

class ForgotPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ('email',)

class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    old_password = serializers.CharField(max_length=255)
    new_password = serializers.CharField(max_length=255)
    confirm_password = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ('email', 'old_password', 'new_password', 'confirm_password')