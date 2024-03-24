from django.contrib import admin
from .models import DeviceModel, Device, Location, Firmware, DataModel, Alert,  Project, Chart, ChartLabel

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ["mac", "model", "location", "latitude", "longitude", "last_call"]
    list_filter = ["model", "location",]

@admin.register(DataModel)
class DataModelAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "model", "reference_tag"]
    list_filter = ["model", ]

@admin.register(DeviceModel)
class DeviceModelAdmin(admin.ModelAdmin):
    list_display = ["name",]

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "address", "latitude", "longitude", "radius"]

@admin.register(Firmware)
class FirmwareAdmin(admin.ModelAdmin):
    list_display = ["model", "version", "detail", "created_at",]
    list_filter = ["model", ]

@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ["project", "name", "formula", "risk"]
    list_filter = ["project", ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ["name", "description"]

@admin.register(Chart)
class ChartAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "project"]

@admin.register(ChartLabel)
class ChartLabelAdmin(admin.ModelAdmin):
    list_display = ["chart", "name", "type", "device", "datamodel"]