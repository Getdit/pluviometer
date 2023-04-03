from core.models import Device

import json


def receive_data(payload, topic):
    mac = topic.split("/")[1].upper()

    device = Device.objects.get(mac=mac)

    if device:
        print(payload)
        message = json.loads(payload)
        version = message["version"]
        message.pop("version")
        print(dir(device))
        device.set_logs(message)

        update_firmware_url = device.model.verify_firmware(version)

        if update_firmware_url:
            from .utils import client
            topic = f"sensor/{mac.lower()}/in"
            client.publish(topic, json.dumps({"update_url":update_firmware_url}))
