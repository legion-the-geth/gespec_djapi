from django.db import models

class Module(models.Model):
    """
    Définition du modèle d'un module
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    libelle = models.CharField(max_length=250)
    # Attributs liés
    formation = models.ForeignKey('formation.Formation', related_name='modules', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.libelle)