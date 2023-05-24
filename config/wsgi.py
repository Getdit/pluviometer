"""
WSGI config for pluviometer project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
#from mqtt.utils import client
# from django.core.wsgi import get_wsgi_application
# from mqtt.utils import client

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# application = get_wsgi_application()

#client.loop_start()