from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    """
    Définition du modèle de profile 
    qui complète l'objet User par défaut de Django
    """
    # Attributs propres
    matricule = models.CharField(max_length=6, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    first_login = models.DateTimeField()
    last_login = models.DateTimeField()
    # Attributs liés
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_on')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()