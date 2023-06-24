from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")

    description = models.TextField(verbose_name="Descrição")

    alert_instructions = models.TextField(verbose_name="Instruções de alerta", default="")

    address = models.CharField(max_length=100, verbose_name="Endereço")

    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")

    radius = models.IntegerField(verbose_name="Raio de cobertura (m)", default=1000)

    def __str__(self):
        return self.name

    def get_lat_str(self):
        return str(self.latitude).replace(",", ".")

    def get_lon_str(self):
        return str(self.longitude).replace(",", ".")

    def in_alert(self):
        alerts = set()
        for p in self.device_set.all():
            for a in p.alert_set.all():
                alerts.add(a)

        for alert in alerts:
            if alert.risk:
                return True
