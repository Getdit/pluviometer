from django.db import models


class DeviceLog(models.Model):
    created_at = models.DateTimeField()
    device = models.ForeignKey("core.Device", on_delete=models.CASCADE, verbose_name="Dispositivo")