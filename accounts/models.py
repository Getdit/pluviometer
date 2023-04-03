from django.db import models

class ResearcherProfile(models.Model):
    phone = models.CharField(max_length=16, verbose_name="Telefone")
    research_institution = models.CharField(max_length=100, verbose_name="Instituição de pesquisa")
    reasearch_area = models.CharField(max_length=150, verbose_name="Área de pesquisa")