from rest_framework import generics
from rest_framework import permissions
from django.contrib.auth.models import User
from perimetre.models import Perimetre
from perimetre.serializers import PerimetreSerializer

class ListePerimetres(generics.ListCreateAPIView):
    queryset = Perimetre.objects.all()
    serializer_class = PerimetreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
    
    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

class DetailPerimetre(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perimetre.objects.all()
    serializer_class = PerimetreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )
