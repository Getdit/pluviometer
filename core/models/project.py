from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome")
    description = models.TextField(blank=True, null=True)