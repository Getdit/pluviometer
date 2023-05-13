from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome")

    description = models.TextField(verbose_name="Descrição")

    address = models.CharField(max_length=100, verbose_name="Endereço")

    latitude = models.FloatField(verbose_name="Latitude")
    longitude = models.FloatField(verbose_name="Longitude")


    def get_lat_str(self):
        return str(self.latitude).replace(",", ".")

    def get_lon_str(self):
        return str(self.longitude).replace(",", ".")
