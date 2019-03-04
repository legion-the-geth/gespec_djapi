from django.db import models

class Personne(models.Model):
    """
    Définition du modèle d'une Personne ou collaborateur de GFI
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    matricule = models.CharField(max_length=10)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s %s (%s)' % (self.prenom, self.nom, self.matricule)