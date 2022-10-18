from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'userinfo')
    phone_no = models.CharField(max_length = 40, null = True, blank = True)
    address = models.CharField(max_length = 100, null = True, blank = True)
    picture = models.ImageField(upload_to = 'account', null = True, blank = True)

    def __str__(self):
        return f"{self.user.username}"
