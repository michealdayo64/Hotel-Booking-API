from django.urls import path
from account import views


app_name = 'account'


urlpatterns = [
    path('register-api/', views.UserCreate.as_view(), name = 'register-api'),
    path('login-api/', views.login_api, name = 'login-api'),
    path('logout-api/', views.logout_api, name = 'logout-api'),
    path('forgot-password-api/', views.forgot_password_api, name = 'forgot-password-api'),
    path('reset-password-api/', views.reset_password_api, name = 'reset-password-api'),
    path('get-user-api/', views.getUserApi, name = 'get-user-api'),
]