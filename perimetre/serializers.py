from rest_framework import serializers
from perimetre.models import Annuaire, Client, Perimetre
from django.contrib.auth.models import User

class AnnuaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annuaire
        fields = ('id', 'created', 'last_modified', 'name', 'host', 'port', 'user', 'pw')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'created', 'last_modified', 'name')

class PerimetreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perimetre
        fields = ('id', 'created', 'last_modified', 'name', 'code')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')