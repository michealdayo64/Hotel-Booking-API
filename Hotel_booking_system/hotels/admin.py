from django.contrib import admin
from .models import Address, Hotel, Facility
# Register your models here.
admin.site.register(Hotel)
admin.site.register(Address)
admin.site.register(Facility)
