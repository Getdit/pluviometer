from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome")
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return f"({self.id}) {self.name}"
