from django.db import models

class Client(models.Model):
    """
    Définition du modèle d'un client
    """
    # Attributs propres
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('-last_modified', '-created')

    def __str__(self):
        return self.name
