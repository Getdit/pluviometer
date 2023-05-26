from django.db import models

class Alert(models.Model):
    name = models.CharField(max_length=40, verbose_name="Nome")

    formula = models.TextField(verbose_name="Formula")

    data_model = models.ForeignKey("core.Device", on_delete=models.CASCADE, verbose_name="Modelo de dados")

    def verify(self):
        return False