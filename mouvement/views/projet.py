from rest_framework import generics, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from mouvement.models import Projet
from mouvement.serializers import ProjetSerializer

class ListeProjets(generics.ListCreateAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DetailProjet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projet.objects.all()
    serializer_class = ProjetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)