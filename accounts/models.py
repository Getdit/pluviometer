from django.db import models

class Profile(models.Model):
    phone = models.CharField(max_length=16, verbose_name="Telefone", null=True, blank=True)

    is_researcher = models.BooleanField(default=False, verbose_name="Pesquisador")
    research_institution = models.CharField(max_length=100, verbose_name="Instituição de pesquisa", null=True, blank=True)
    reasearch_area = models.CharField(max_length=150, verbose_name="Área de pesquisa", null=True, blank=True)

    projects = models.ManyToManyField('core.Project', verbose_name="Projetos (como bolsista)", blank=True, related_name="users")

    owner = models.OneToOneField('auth.User', on_delete=models.CASCADE, verbose_name="Usuário")
    active = models.BooleanField(default=False, verbose_name="Ativo")

    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def get_full_name(self):
        return self.owner.get_full_name()