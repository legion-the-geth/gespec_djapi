from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from mouvement.models import Personne
from mouvement.serializers import PersonneSerializer

class ListePersonnes(generics.ListCreateAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    permission_classes = (permissions.IsAuthenticated,)

class DetailPersonne(generics.RetrieveUpdateDestroyAPIView):
    queryset = Personne.objects.all()
    serializer_class = PersonneSerializer
    permission_classes = (permissions.IsAuthenticated,)