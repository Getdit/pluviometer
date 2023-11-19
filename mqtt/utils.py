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
            print(f"sensor/{device.mac.upper()}/out")
            mqtt_client.subscribe(f"sensor/{device.mac.upper()}/out")
    else:
        raise NameError("MQTT Connect error: {}".format(rc))


def on_message(client, userdata, msg):
    flag = True
    while flag:
        try:
            from .views import receive_data
            flag = False
        except:
            print("Erro ao importar receive_data")
            pass
    print(client, userdata, msg)
    receive_data(msg.payload.decode('utf-8'), msg.topic)

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=settings.BROKER_ADDRESS, port=settings.BROKER_PORT)
except Exception as e:
    print(e)
    client = None