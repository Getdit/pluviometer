from django.contrib import admin
from .models import Profile


admin.site.site_header = "Administração do Sistema"

admin.site.register(Profile)