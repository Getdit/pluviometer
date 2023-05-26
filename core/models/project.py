from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=40, verbose_name="Nome")
    description = models.TextField(verbose_name="Descrição")

    participants = models.ManyToManyField("accounts.Profile", verbose_name="Participantes")