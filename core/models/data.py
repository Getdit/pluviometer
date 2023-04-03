from django.db import models


class Data(models.Model):
    log = models.ForeignKey("core.DeviceLog", on_delete=models.CASCADE, related_name="datalog_set", verbose_name="Log")
    model = models.ForeignKey("core.DataModel", on_delete=models.CASCADE, verbose_name="Modelo")

    value = models.IntegerField(verbose_name="Valor", blank=True, null=True)