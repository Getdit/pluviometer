from django.db import models


class Device(models.Model):
    mac = models.CharField(max_length=30, verbose_name="MAC")
    model = models.ForeignKey("core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")

    last_call = models.DateTimeField(verbose_name="Última chamada")

    location = models.ForeignKey("core.Location", on_delete=models.CASCADE, verbose_name="Local")
    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    project = models.ManyToManyField("core.Project", verbose_name="Projeto", null=True)

    graph_data_models = models.ManyToManyField("core.DataModel", verbose_name="Modelos de dados para o gráfico", blank=True)

    def save(
        self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        r = super(Device, self).save()
        from mqtt.utils import client
        if client:
            client.subscribe(f"sensor/{self.mac.lower()}/out")
        return r

    def __str__(self):
        return f"{self.location}: {self.model} - {self.mac} "

    def set_logs(self, data):
        log = self.devicelog_set.create(device=self.id)

        for model_data in self.model.datamodel_set.all():
            if model_data.reference_tag in data.keys():
                log.datalog_set.create(
                    log=log,
                    model=model_data,
                    value=data[model_data.reference_tag]
                )

        self.last_call = log.timestamp
        self.save()

        self.verify_alerts()

    def verify_alerts(self):
        for alert in self.project.alert_set.all():
            alert.verify()