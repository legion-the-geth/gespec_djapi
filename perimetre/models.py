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
    manager = models.ForeignKey('auth.User', related_name='perimetres', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='perimetres', on_delete=models.CASCADE)
    annuaire = models.ForeignKey(Annuaire, related_name='perimetres', on_delete=models.SET(Annuaire.get_sentinel_ad))

    def __str__(self):
        return '%s (%s)' % (self.name, self.code)

    class Meta:
        ordering = ('-last_modified', '-created')

class Client(models.Model):
    """
    Définition du modèle d'un client
    """
    # Attributs propres
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-last_modified', '-created')

class Annuaire(models.Model):
    """
    Définition du modèle d'un Annuaire de type AD ou LDAP
    """
    # Attributs propres
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)
    port = models.CharField(max_length=5)
    user = models.CharField(max_length=50)
    pw = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def get_sentinel_ad():
        return Annuaire.objects.get_or_create(name='default')[0]

    class Meta:
        ordering = ('-last_modified', '-created')

