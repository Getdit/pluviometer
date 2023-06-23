from django.db import models

class Alert(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome")
    description = models.TextField(blank=True, null=True)

    formula = models.CharField(max_length=90, verbose_name="Fórmula")

    project = models.ForeignKey("core.Project", on_delete=models.CASCADE, verbose_name="Projeto")
    devices = models.ManyToOneRel("core.Device", on_delete=models.CASCADE, verbose_name="Dispositivos para os quais o alerta se aplica")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Alerta"
        verbose_name_plural = "Alertas"
