from rest_framework import serializers
from perimetre.models import Perimetre, Annuaire, Client
from django.contrib.auth.models import User

class PerimetreSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    annuaire = serializers.PrimaryKeyRelatedField(queryset=Annuaire.objects.all())
    
    class Meta:
        model = Perimetre
        fields = ('id', 'created', 'last_modified', 'name', 'manager', 'client', 'annuaire')

class AnnuaireSerializer(serializers.ModelSerializer):
    # perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Perimetre.objects.all(), read_only=True)
    
    class Meta:
        model = Annuaire
        fields = ('id', 'created', 'last_modified', 'name', 'host', 'port', 'user', 'pw')

class ClientSerializer(serializers.ModelSerializer):
    # perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Perimetre.objects.all(), read_only=True)
    
    class Meta:
        model = Client
        fields = ('id', 'created', 'last_modified', 'name')