from django.db import models
from enum import Enum
from django.utils.translation import gettext as _
from mouvement.models import Personne

class Formation(models.Model):
    """
    Définition du modèle d'une formation Gfi
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    libelle = models.CharField(max_length=250)
    # Attributs liés
    nature = models.ForeignKey('formation.nature', related_name='formations', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.libelle)
