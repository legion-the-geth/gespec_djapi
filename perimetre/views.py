from rest_framework import generics
from perimetre.models import Annuaire, Client, Perimetre
from perimetre.serializers import AnnuaireSerializer, ClientSerializer, PerimetreSerializer

class ListePerimetres(generics.ListCreateAPIView):
    """
    Liste tous les périmètres ou en ajoute un nouveau à la collection.
    """
    queryset = Perimetre.objects.all()
    serializer_class = PerimetreSerializer

class DetailPerimetre(generics.RetrieveUpdateDestroyAPIView):
    """
    Récupère, modifie ou supprime un périmètre
    """
    queryset = Perimetre.objects.all()
    serializer_class = PerimetreSerializer

class ListeAnnuaires(generics.ListCreateAPIView):
    """
    Liste tous les périmètres ou en ajoute un nouveau à la collection.
    """
    queryset = Annuaire.objects.all()
    serializer_class = AnnuaireSerializer

class DetailAnnuaire(generics.RetrieveUpdateDestroyAPIView):
    """
    Récupère, modifie ou supprime un périmètre
    """
    queryset = Annuaire.objects.all()
    serializer_class = AnnuaireSerializer

class ListeClients(generics.ListCreateAPIView):
    """
    Liste tous les périmètres ou en ajoute un nouveau à la collection.
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class DetailClient(generics.RetrieveUpdateDestroyAPIView):
    """
    Récupère, modifie ou supprime un périmètre
    """
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
