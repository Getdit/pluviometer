from django.urls import path
from .views import mqtt_message, mqtt_get_devices

app_name = 'mqtt'

urlpatterns = [
    path('communication/', mqtt_message, name='communication'),
    path('get-devices/', mqtt_get_devices, name='communication'),
]