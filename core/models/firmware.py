from django.db import models
from django.utils.crypto import get_random_string

def upload_to(instance, filename):
    return f"firmwares/products/firm_{get_random_string(6)}_{str(instance.version)}{filename[filename.index('.'):]}"

class Firmware(models.Model):
    file = models.FileField(upload_to=upload_to, verbose_name="Arquivo")
    version = models.IntegerField(verbose_name="Versão")
    detail = models.TextField("Detalhes da versão", default="")

    model = models.ForeignKey("core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")

    created_at = models.DateTimeField(auto_now=True, blank=True)