from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from mouvement.models import Mouvement
from mouvement.serializers import MouvementSerializer

class ListeMouvements(generics.ListCreateAPIView):
    queryset = Mouvement.objects.all()
    serializer_class = MouvementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )

class DetailMouvement(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mouvement.objects.all()
    serializer_class = MouvementSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, )