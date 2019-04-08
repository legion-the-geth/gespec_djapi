from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from formation.models import Formation
from formation.serializers import FormationSerializer

class ListeFormations(generics.ListCreateAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
    permission_classes = (permissions.IsAuthenticated, )

class DetailFormation(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formation.objects.all()
    serializer_class = FormationSerializer
    permission_classes = (permissions.IsAuthenticated, )