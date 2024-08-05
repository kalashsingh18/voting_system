from rest_framework import serializers
from .models import candiates,create_elections
class Candidatesserializer(serializers.ModelSerializer):
    class Meta:
        model=candiates
        fields="__all__"
class Create_elections_serializer(serializers.ModelSerializer):
    class Meta:
        model=create_elections
        fields="__all__"
