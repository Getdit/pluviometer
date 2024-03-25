from django.db import models
from django.utils import timezone

class DeviceLog(models.Model):
    # created_at can or not recive a value from the user
    created_at = models.DateTimeField(verbose_name="Criado em")
    device = models.ForeignKey("core.Device", on_delete=models.CASCADE, verbose_name="Dispositivo")

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        if not self.created_at:
            self.created_at = timezone.now()

        super().save()