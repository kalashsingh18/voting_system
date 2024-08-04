from django.shortcuts import render
from .serializer import Candidatesserializer
# Create your views here.

from .models import candiates
from rest_framework import generics
class create_candidates(generics.CreateAPIView):
        queryset=candiates.objects.all()
        serializer_class=Candidatesserializer
