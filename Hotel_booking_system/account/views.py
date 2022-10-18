from django.shortcuts import render
from .serializers import UserInfoSerializer, UserSerializer, ForgotPasswordSerializer, ResetPasswordSerializer
from .models import UserInfo
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from passlib.hash import django_pbkdf2_sha256 as handler
from django.conf import settings
from django.core.mail import send_mail
import random
# Create your views here.


def index(request):
    return render(request, 'index.html')

# -------------------------------------------> API SECTION <------------------------------------------------

# REGISTER API
class UserCreate(APIView):
    permission_classes = (AllowAny, )
    def post(self, request):
        data = {}
        user_data = UserSerializer(data = request.data or None)
        phone_no = request.data.get('phone_no')
        address = request.data.get('address')
        if user_data.is_valid():
            user = user_data.save()
            user.set_password(user.password)
            user.save()

            # CREATE TOKEN
            Token.objects.create(user = user)
            
            # CREATE USER INFO
            UserInfo.objects.create(
                user = user,
                phone_no = phone_no,
                address = address
            )
            data['msg'] = "Register Successfully"
            return Response(data = data, status = status.HTTP_200_OK)
        data['error'] = 'Something is wrong'
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

# LOGIN API
@api_view(['POST',])
@permission_classes((AllowAny,))
def login_api(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username = username, password = password)
    if user:
        if user.is_active:
            login(request, user)
            data = {
                'msg': "Login Successfully",
                "token": user.auth_token.key
            }
            return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            "msg": "Username or Password Incorrect"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

# LOGOUT API    
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def logout_api(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        data = {
            "msg": f"{user.username} Logged out Successfully"
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            "msg": "Authentication not valid"
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)

# FORGOT PASSWORD
@api_view(['POST',])
@permission_classes((AllowAny,))
def forgot_password_api(request):
    serializer = ForgotPasswordSerializer(data = request.data or None)
    # Generating Random Password of specific Type or use according to your need
    str_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z']
    str_2 = ['!', '@', '#', '$', '%', '&', '*', '/', '-', '+']
    str_3 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    str = random.choice(str_1)
    for s in range(4):
        str += random.choice(str_1).lower()
    str += random.choice(str_2)
    for x in range(2):
        str += random.choice(str_3)

    password = handler.hash(str)
    
    if serializer.is_valid():
        email = request.data['email']
        print(email)
        User.objects.filter(email=email).update(password=password)

        subject = 'Forgot Password Request'
        message = 'Your request for Forgot Password has been received, your new password is ' + str
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email]

        send_mail(
            subject,
            message,
            email_from,
            recipient_list,
            fail_silently=False,
        )
        data = {
            'msg': 'done'
        }
        return Response(data = data, status=status.HTTP_200_OK)
    else:
        data = {
            'msg': 'Not a valid request'
        }
        return Response(data = data, status=status.HTTP_400_BAD_REQUEST)

# RESET PASSWORD
'''@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def reset_password_api(request):
    user = request.user
    serializer = ResetPasswordSerializer(data=request.data)
    if serializer.is_valid():
        new_password = request.data['new_password']
        confirm_password = request.data['confirm_password']
        if new_password == confirm_password:
            password = handler.hash(new_password)
            email = request.data['email']
            User.objects.get(username=user,).update(password=password)
            data = {
                'Success': 'Password updated successfully'
            }
            return Response(data = data, status=status.HTTP_200_OK)
        else:
            data = {
                'msg': 'New Password and Confirm Password does not match, please enter again'
            }
            return Response(data = data, status=status.HTTP_409_CONFLICT)
    else:
        data = {
            'msg': 'Invalid request'
        }
        return Response(data = data, status=status.HTTP_400_BAD_REQUEST)'''

# RESET PASSWORD
@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def reset_password_api(request):
    user = request.user.pk
    
    email = request.data.get('password')
    old_password = request.data.get('old_password')
    new_password = request.data.get('new_password')
    confirm_password = request.data.get('confirm_password')

    user = User.objects.get(pk = user)
    #print(user.check_password(old_password))
    if not user.check_password(old_password):
        data = {
             "msg": "Your old password is wrong"
        }   
    if new_password == confirm_password:
        user.set_password(new_password)
        user.save()
        
        data = {
            "msg": "password changed successfully"
        }
        return Response(data = data, status = status.HTTP_200_OK)
    else:
        data = {
            'msg': 'Password does not match'
        }
        return Response(data = data, status = status.HTTP_400_BAD_REQUEST)


#GET USER
@api_view(['GET',])
@permission_classes((IsAuthenticated,))
def getUserApi(request):
    user = request.user.id
    
    get_user = UserInfo.objects.get(user = user)
    
    userdata = UserInfoSerializer(get_user)
    #print(get_user)
    if userdata:
        data = {
            'msg': userdata.data
        }
        return Response(data = data, status=status.HTTP_200_OK)  
    data = {
        "msg": "Failed to fecth user"
    } 
    return Response(data = data, status=status.HTTP_400_BAD_REQUEST)