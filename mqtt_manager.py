import requests
import json
import paho.mqtt.client as mqtt

BROKER_ADDRESS = "150.162.235.160"#"localhost"
BROKER_PORT = 8004

def on_connect(mqtt_client, userdata, flags, rc):
    if rc == 0:
        devices = requests.get("http://127.0.0.1:4200/mqtt/get-devices/").json()['devices']
        for device in devices:
            print(f"sensor/{device}/out")
            mqtt_client.subscribe(f"sensor/{device}/out")
        print("MQTT Client started")
    else:
        raise NameError("MQTT Connect error: {}".format(rc))


def on_message(client, userdata, msg):
    requests.post('http://127.0.0.1:4200/mqtt/communication/', data={"payload":msg.payload.decode('utf-8'), "topic":msg.topic})

try:
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host=BROKER_ADDRESS, port=BROKER_PORT)
    client.loop_forever()

except Exception as e:
    print(e)
    client = None

