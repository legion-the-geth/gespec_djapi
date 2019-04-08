from rest_framework import generics, permissions, renderers
from rest_framework.decorators import action
from rest_framework.response import Response
from formation.models import Module
from formation.serializers import ModuleSerializer

class ListeModules(generics.ListCreateAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (permissions.IsAuthenticated,)

class DetailModule(generics.RetrieveUpdateDestroyAPIView):
    queryset = Module.objects.all()
    serializer_class = ModuleSerializer
    permission_classes = (permissions.IsAuthenticated,)