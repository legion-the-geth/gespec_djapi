from django.db import models

class Mouvement(models.Model):
    """
    Définition du modèle d'un mouvement
    """
    # Attributs propres
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100, blank=True, default='inconnu')

    def __str__(self):
        return 'myName'

    def get_sentinel_movt():
        return Mouvement.objects.get_or_create(name='inconnu')[0]

    class Meta:
        ordering = ('-last_modified', '-created')