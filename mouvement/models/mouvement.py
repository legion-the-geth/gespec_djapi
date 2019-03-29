from django.db import models
from enum import Enum
from django.utils.translation import gettext as _
from perimetre.models import Perimetre
from mouvement.models import Machine, Mobile, Projet, Personne

class TypeMouvement(Enum):
    personne = "P"
    asset = "A"

class Mouvement(models.Model):
    """
    Définition du modèle d'un mouvement
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    type_mouvmt = models.CharField(max_length=2, choices=[
        (TypeMouvement.personne, _('Mouvement de personne')),
        (TypeMouvement.asset, _('Mouvement d\'asset')),
    ])
    zedmail = models.BooleanField(default=False)
    cle_rsa = models.BooleanField(default=False)
    # Attributs liés
    # 1-n
    perimetre = models.ForeignKey(Perimetre, related_name='mouvements', blank=True, null=True, on_delete=models.SET_NULL)
    projet = models.ForeignKey(Projet, related_name='mouvements', blank=True, null=True, on_delete=models.SET_NULL)
    personne = models.ForeignKey(Personne, related_name='mouvements', blank=True, null=True, on_delete=models.SET_NULL)
    # n-n
    machines = models.ManyToManyField(Machine, related_name='mouvements')
    mobiles = models.ManyToManyField(Mobile, related_name='mouvements')

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.created_at)
