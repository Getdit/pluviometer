from core.models import Device
from django.http.response import JsonResponse, HttpResponse

import json
from json.decoder import JSONDecodeError
from django.views.decorators.csrf import csrf_exempt

PRINT_DATA = False

@csrf_exempt
def mqtt_message(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f"IP: {ip}")
    if ip == '127.0.0.1':
        print(request.POST, request.FILES, request.GET, request)
        receive_data(payload=request.POST.get('payload'), topic=request.POST.get('topic'))
    return HttpResponse()

def mqtt_get_devices(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    print(f"IP: {ip}")
    if ip == '127.0.0.1':
        return JsonResponse({"devices": [d.mac.upper() for d in Device.objects.all()]})

def receive_data(payload, topic):
    if PRINT_DATA:
        print(payload, topic)
    mac = topic.split("/")[1].upper()

    device = Device.objects.filter(mac=mac).first()

    if device:
        try:
            message = json.loads(payload)
            version = message["version"]
            message.pop("version")

            datetime = None
            if "datetime" in message.keys():
                datetime = message["datetime"]
                message.pop("datetime")
                if PRINT_DATA:
                    print(f"VERSÂO: {version}  DATETIME: {datetime}   MESSAGE: {message}")
            device.set_logs(message, datetime)

            update_firmware_url = device.model.verify_firmware(version)

            if update_firmware_url:
                from .utils import client
                topic = f"sensor/{mac.lower()}/in"
                client.publish(topic, json.dumps({"update_url":update_firmware_url}))
        except JSONDecodeError:
            print(f"DecodeError: {mac}")
