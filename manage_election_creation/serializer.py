from rest_framework import serializers
from .models import candiates
class Candidatesserializer(serializers.ModelSerializer):
    class Meta:
        model=candiates
        fields="__all__"
