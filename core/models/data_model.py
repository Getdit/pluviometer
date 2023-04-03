from django.db import models


class DataModel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nome do dado")
    description = models.TextField(verbose_name="Descrição")

    model = models.ForeignKey("core.DeviceModel", on_delete=models.CASCADE, verbose_name="Modelo")
    reference_tag = models.CharField(max_length=30, verbose_name="Tag de referência")

    alert_per_time = models.TimeField(verbose_name="Alerta por período (vazio para alerta por valor)", null=True, blank=True)
    warning_alert = models.FloatField(verbose_name='Valor mínimo para "Alerta"')
    danger_alert = models.FloatField(verbose_name='Valor mínimo para "Perigo"')
