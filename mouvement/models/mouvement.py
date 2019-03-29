from django.db import models
from perimetre.models import Perimetre
from mouvement.models import Machine, Mobile, Projet

class Mouvement(models.Model):
    """
    Définition du modèle d'un mouvement
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    # Attributs liés
    perimetre = models.ForeignKey(Perimetre, related_name='mouvements', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.created_at)
