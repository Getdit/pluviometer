import paho.mqtt.client as mqtt
from django.conf import settings


def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        flag = True
        while flag:
            try:
                from core.models import Device
                flag = False
            except:
                pass
        for device in Device.objects.all():
            mqtt_client.subscribe(f"sensor/{device.mac.lower()}/out")
    else:
        raise NameError("MQTT Connect error: {}".format(rc))


def on_message(client, userdata, msg):
    flag = True
    while flag:
        try:
            from .views import receive_data
            flag = False
        except:
            pass
    receive_data(msg.payload.decode('utf-8'), msg.topic)

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=settings.BROKER_ADDRESS, port=1883)
except Exception as e:
    print(e)
    client = None