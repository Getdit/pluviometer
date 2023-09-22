"""
WSGI config for pluviometer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()

flag = True
while flag:
    try:
        from mqtt.utils import client
        client.loop_start()
        flag = False
    except:
        pass
print("MQTT Client started")