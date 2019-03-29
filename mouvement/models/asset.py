from django.db import models
from enum import Enum
from django.utils.translation import gettext as _

class StatutAsset(Enum):
    sans_affectation = "SA"
    disponible = "DISP"
    sorti = "OUT"
    affecte = "AFF"
    affecte_conforme = "CONF"

class Asset(models.Model):
    """
    Définition du modèle abstrait d'un asset
    Ce modèle est utilisé comme classe abstraite de base pour les modèles des Machines (PC) ou des Mobiles.
    """
    # Attributs propres
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    code = models.CharField(max_length=10)
    os = models.CharField(max_length=25)
    premiere_mes = models.DateTimeField(blank=True, null=True)
    statut = models.CharField(max_length=10, choices=[
        (StatutAsset.sans_affectation, _('Sans affectation')),
        (StatutAsset.disponible, _('Disponible pour affectation')),
        (StatutAsset.sorti, _('Sorti du périmètre')),
        (StatutAsset.affecte, _('Affecté')),
        (StatutAsset.affecte_conforme, _('Affecté et conforme')),
    ])
    conforme = models.BooleanField(default=False)
    # Attributs liés

    class Meta:
        abstract = True

class Machine(Asset):
    """
    Définition du modèle d'une machine (PC, Mac...)
    """
    # Attributs propres
    # Attributs liés

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.code)

class Mobile(Asset):
    """
    Définition du modèle d'un Mobile (Android, IPhone...)
    """
    # Attributs propres
    numero_ligne = models.CharField(max_length=25)
    operateur = models.CharField(max_length=50)
    forfait = models.CharField(max_length=100)
    # Attributs liés

    class Meta:
        ordering = ('-modified_at', '-created_at')

    def __str__(self):
        return '%s' % (self.code)