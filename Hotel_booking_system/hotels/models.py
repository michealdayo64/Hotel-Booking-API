from django.db import models

# Create your models here.
class Facility(models.Model):
    facility = models.CharField(max_length = 20, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.facility}"

class Address(models.Model):
    city = models.CharField(max_length = 20, null = True, blank = True)
    pinCode = models.CharField(max_length = 20, null = True, blank = True)
    state = models.CharField(max_length = 20, null = True, blank = True)
    streetNo = models.CharField(max_length = 20, null = True, blank = True)
    landmark = models.CharField(max_length = 20, null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.state

class Hotel(models.Model):
    hotel_name = models.CharField(max_length = 300, null = True, blank = True)
    hotel_image = models.ImageField(upload_to = 'hotel', blank = True, null = True)
    slug = models.SlugField(default = '')
    addrees = models.ForeignKey(Address, on_delete = models.CASCADE, blank = True, null = True, related_name = 'address')
    facilities = models.ManyToManyField(Facility)
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.hotel_name
    
