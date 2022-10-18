from django.urls import path
from rooms import views


app_name = 'rooms'

urlpatterns = [
    path('room_list/', views.room_list_api, name = 'room_list'),
    path('roomtype_list/', views.roomtype_list_api, name = 'roomtype_list'),
]