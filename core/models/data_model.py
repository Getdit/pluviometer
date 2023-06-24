from django.db import models


class DataModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do dado")
    description = models.TextField(verbose_name="Descrição")

    model = models.ForeignKey(
        "core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")
    reference_tag = models.CharField(
        max_length=30, verbose_name="Tag de referência")

