from rest_framework import serializers
from django.contrib.auth.models import User
from mouvement.models import Mouvement, Personne, Machine, Mobile

class MouvementSerializer(serializers.HyperlinkedModelSerializer):
    manager = serializers.HyperlinkedRelatedField(queryset=User.objects.all(), view_name='detail-user')

    class Meta:
        model = Mouvement
        fields = ('id', 'created', 'last_modified', 'name', 'code', 'manager')

class UserSerializer(serializers.ModelSerializer):
    perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Mouvement.objects.all())
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'perimetres')

class AnnuaireSerializer(serializers.HyperlinkedModelSerializer):
    perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Mouvement.objects.all())

    class Meta:
        model = Annuaire
        fields = ('id', 'created', 'last_modified', 'name', 'host', 'port', 'user', 'pw', 'perimetres')

class ClientSerializer(serializers.HyperlinkedModelSerializer):
    perimetres = serializers.PrimaryKeyRelatedField(many=True, queryset=Mouvement.objects.all())

    class Meta:
        model = Client
        fields = ('id', 'created', 'last_modified', 'name', 'perimetres')
