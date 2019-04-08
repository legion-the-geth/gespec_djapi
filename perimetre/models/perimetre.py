from django.db import models
from perimetre.models import Client, Annuaire

class Perimetre(models.Model):
    """
    Définition du modèle d'un périmètre de conformité.
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=5)
    # Attributs liés
    manager = models.ForeignKey('auth.User', related_name='perimetres', blank=True, null=True, on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='perimetres', blank=True, null=True, on_delete=models.SET_NULL)
    annuaire = models.ForeignKey(Annuaire, related_name='perimetres', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)
