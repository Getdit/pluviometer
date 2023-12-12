# flag = True
# print("MQTT init")
# while flag:
#     try:
#         from django.conf import settings
#         settings.STARTED_MQTT = getattr(settings, 'STARTED_MQTT', False)
#         if not settings.STARTED_MQTT:
#             settings.STARTED_MQTT = True
#             from mqtt.utils import client
#             client.loop_start()
#             print("MQTT Client started")
#         flag = False
#     except:
#         pass
