from django.db import models


class DeviceLog(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    device = models.ForeignKey("core.Device", on_delete=models.CASCADE, verbose_name="Dispositivo")