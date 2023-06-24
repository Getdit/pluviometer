from django.db import models

class Profile(models.Model):
    phone = models.CharField(max_length=16, verbose_name="Telefone")

    is_researcher = models.BooleanField(default=False, verbose_name="Pesquisador")
    research_institution = models.CharField(max_length=100, verbose_name="Instituição de pesquisa")
    reasearch_area = models.CharField(max_length=150, verbose_name="Área de pesquisa")

    projects = models.ManyToManyField('core.Project', verbose_name="Projetos (como bolsista)", blank=True, related_name="users")

    owner = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name="Usuário")

    def get_full_name(self):
        return self.owner.get_full_name()