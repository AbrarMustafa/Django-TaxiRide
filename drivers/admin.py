from django.contrib import admin
from .models import DriverProfile, VehicleComfortOption, DriverCar

admin.site.register(DriverProfile)
admin.site.register(VehicleComfortOption)
admin.site.register(DriverCar)