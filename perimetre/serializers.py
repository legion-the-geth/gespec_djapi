from rest_framework import serializers
from django.contrib.auth.models import User
from perimetre.models import Annuaire, Client, Perimetre

class PerimetreSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='detail-user')

    class Meta:
        model = Perimetre
        fields = ('id', 'created_at', 'modified_at', 'name', 'code', 'manager')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class AnnuaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Annuaire
        fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'
