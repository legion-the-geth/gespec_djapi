from django.db import models

class Client(models.Model):
    """
    Définition du modèle d'un client
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return self.name
