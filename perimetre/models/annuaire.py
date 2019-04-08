from django.db import models

class Annuaire(models.Model):
    """
    Définition du modèle d'un Annuaire de type AD ou LDAP
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='inconnu')
    host = models.CharField(max_length=100, blank=True, null=True)
    port = models.CharField(max_length=5, blank=True, null=True)
    user = models.CharField(max_length=50, blank=True, null=True)
    pw = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return self.name

