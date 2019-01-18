from django.db import models

class Perimetre(models.Model):
    """
    Définition du modèle d'un périmètre de conformité.
    """
    # Attributs propres
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    code = models.TextField(max_length=5, default=name[:5])
    # Attributs liés
    manager = models.ForeignKey('auth.User', related_name='perimetres', on_delete=models.SET_NULL)
    client = models.ForeignKey(Client, related_name='perimetres', on_delete=models.SET(Annuaire.get_sentinel_client))
    annuaire = models.ForeignKey(Annuaire, related_name='perimetres', on_delete=models.SET(Annuaire.get_sentinel_ad))

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    class Meta:
        ordering = ('-last_modified', '-created')
