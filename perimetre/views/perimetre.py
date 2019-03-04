from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework.response import Response
from django.contrib.auth.models import User
from perimetre.models import Perimetre
from perimetre.serializers import PerimetreSerializer
from perimetre.permissions import ManagerPerimOrReadOnly

class ListePerimetres(generics.ListCreateAPIView):
    queryset = Perimetre.objects.all()
    serializer_class = PerimetreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, ManagerPerimOrReadOnly)
    
    def perform_create(self, serializer):
        serializer.save(manager=self.request.user)

class DetailPerimetre(generics.RetrieveUpdateDestroyAPIView):
    queryset = Perimetre.objects.all()
    serializer_class = PerimetreSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class DetailPerimetreHtml(generics.GenericAPIView):
    queryset = Perimetre.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        perimetre = self.get_object()
        return Response(perimetre.manager)