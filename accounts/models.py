from django.db import models

class PROFILE_TYPES(models.TextChoices):
    r = ("r", "Pesquisador(a)")
    b = ("b", "Bolsista")
    u = ("u", "Indefinido")
class Profile(models.Model):
    profile_type = models.CharField(max_length=1, default="u", choices=PROFILE_TYPES.choices, verbose_name="Tipo de perfil")
