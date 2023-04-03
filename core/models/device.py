from django.db import models


class Device(models.Model):
    mac = models.CharField(max_length=12, verbose_name="MAC")
    model = models.ForeignKey("core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")

    last_call = models.DateTimeField(verbose_name="Última chamada")

    location = models.ForeignKey("core.Location", on_delete=models.CASCADE, verbose_name="Local")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        r = super(Device, self).save()
        from mqtt.utils import client
        if client:
            client.subscribe(f"sensor/{self.mac.lower()}/out")
        return r

    def set_logs(self, data):
        log = self.devicelog_set.create(device=self.id)

        for model_data in self.model.datamodel_set.all():
            if model_data.reference_tag in data.keys():
                log.datalog_set.create(
                    log=log,
                    model=model_data,
                    value=data[model_data.reference_tag]
                )
