from django.urls import path
from hotels import views


app_name = 'hotels'

urlpatterns = [
    path('facility_list/', views.facility_list_api, name = 'facility_list'),
    path('hotel_list/', views.hotel_list_api, name = 'hotel_list'),
    path('address_list/', views.address_list_api, name = 'address_list'),
    path('hotel_rooms/', views.hotel_id_api, name = 'hotel_rooms'),
    path('hotel_id/<id>/', views.hotel_id_api, name = 'hotel-id')
]