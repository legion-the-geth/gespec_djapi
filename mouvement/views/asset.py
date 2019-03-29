from rest_framework import generics, permissions, renderers
from rest_framework.response import Response
from mouvement.models import Machine, Mobile
from mouvement.serializers import MachineSerializer, MobileSerializer

# Machines
class ListeMachines(generics.ListCreateAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DetailMachine(generics.RetrieveUpdateDestroyAPIView):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

# Mobiles
class ListeMobiles(generics.ListCreateAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

class DetailMobile(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mobile.objects.all()
    serializer_class = MobileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)