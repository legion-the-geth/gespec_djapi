from rest_framework import serializers
from django.contrib.auth.models import User
from perimetre.models import Annuaire, Client, Perimetre

class PerimetreSerializer(serializers.ModelSerializer):
    manager = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Perimetre
        fields = ('id', 'created', 'last_modified', 'name', 'code', 'manager')

class UserSerializer(serializers.ModelSerializer):
    perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Perimetre.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'perimetres')

class AnnuaireSerializer(serializers.ModelSerializer):
    perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Perimetre.objects.all())

    class Meta:
        model = Annuaire
        fields = ('id', 'created', 'last_modified', 'name', 'host', 'port', 'user', 'pw', 'perimetres')

class ClientSerializer(serializers.ModelSerializer):
    perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Perimetre.objects.all())

    class Meta:
        model = Client
        fields = ('id', 'created', 'last_modified', 'name', 'perimetres')