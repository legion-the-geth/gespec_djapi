from rest_framework import serializers
from django.contrib.auth.models import User
from mouvement.models import Mouvement, Projet, Personne, Machine, Mobile
from perimetre.models import Perimetre, Annuaire, Client

class MouvementSerializer(serializers.HyperlinkedModelSerializer):
    perimetre = serializers.HyperlinkedRelatedField(queryset=Perimetre.objects.all(), view_name='detail-perimetre')
    projet = serializers.HyperlinkedRelatedField(queryset=Projet.objects.all(), view_name='detail-projet')
    personne = serializers.HyperlinkedRelatedField(queryset=Personne.objects.all(), view_name='detail-personne')

    class Meta:
        model = Mouvement
        fields = ('id', 
            'created_at', 
            'modified_at', 
            'type_mouvmt', 
            'zedmail', 
            'cle_rsa',
            'perimetre', 
            'projet', 
            'personne',
        )

class ProjetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projet
        fields = '__all__'

class PersonneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personne
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = '__all__'
