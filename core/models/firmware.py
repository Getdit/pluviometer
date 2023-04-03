from django.db import models

def upload_to(instance, filename):
    return f"firmwares/products/firm_{str(instance.model.id)}_{str(instance.version)}{filename[filename.index('.'):]}"

class Firmware(models.Model):
    file = models.FileField(upload_to=upload_to, verbose_name="Arquivo")
    version = models.IntegerField(verbose_name="Versão")
    detail = models.TextField("Detalhes da versão", default="")

    model = models.ForeignKey("core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")

    created_at = models.DateTimeField(auto_now=True, blank=True)