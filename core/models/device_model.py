from django.db import models


class DeviceModel(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome")

    class Meta:
        verbose_name = "Modelo de dispositivo"
        verbose_name_plural = "Modelos de dispositivo"

    def __str__(self):
        return self.name

    def verify_firmware(self, version):
        last_fw = self.firmware_set.all().order_by("-version").first()

        if (not last_fw is None) and last_fw.version > version:
            from core.models import TempURL
            temp_url = TempURL.objects.create(
                path=last_fw.file.path
            )
            return temp_url.get_absolute_url()
        return
