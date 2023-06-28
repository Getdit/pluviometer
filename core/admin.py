from django.contrib import admin
from .models import DeviceModel, Device, Location, Firmware, DataModel, Alert, Data, Project

admin.site.register(Device)
admin.site.register(DataModel)
admin.site.register(DeviceModel)
admin.site.register(Location)
admin.site.register(Firmware)
admin.site.register(Alert)
admin.site.register(Data)
admin.site.register(Project)
