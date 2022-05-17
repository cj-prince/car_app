from django.contrib import admin
from .models import Manufacturer, Car, Feature, CarProfile

# Register your models here.
admin.site.register((Manufacturer, Car, Feature, CarProfile))