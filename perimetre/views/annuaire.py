from rest_framework import generics
from rest_framework import permissions
from perimetre.models import Annuaire
from perimetre.serializers import AnnuaireSerializer

class ListeAnnuaires(generics.ListCreateAPIView):
    queryset = Annuaire.objects.all()
    serializer_class = AnnuaireSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class DetailAnnuaire(generics.RetrieveUpdateDestroyAPIView):
    queryset = Annuaire.objects.all()
    serializer_class = AnnuaireSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
