from django.db import models
from mouvement.models import Personne
from perimetre.models import Perimetre

class Projet(models.Model):
    """
    Définition du modèle d'un projet
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    nom = models.CharField(max_length=100)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    # Attributs liés
    responsable = models.ForeignKey(Personne, related_name='projets', blank=True, null=True, on_delete=models.SET_NULL)
    perimetre = models.ForeignKey(Perimetre, related_name='projets', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.nom)