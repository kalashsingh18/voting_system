from rest_framework import serializers
from .models import users
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class Users_models_serializer(serializers.ModelSerializer):
    class Meta:
        model = users
        fields = "__all__"

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, users):
        
        token = super().get_token(users)
        # Add custom claims
        token['username'] = users.username
        return token
