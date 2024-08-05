from django.shortcuts import render
from .serializer import Candidatesserializer,Create_elections_serializer
import hashlib
from rest_framework.response import Response
from .models import candiates
from rest_framework.decorators import api_view
from .models import candiates,create_elections
from rest_framework import generics
class create_candidates(generics.ListCreateAPIView):
        queryset=candiates.objects.all()
        serializer_class=Candidatesserializer
class create_elections(generics.CreateAPIView):
        queryset=create_elections.objects.all()
        serializer_class=Create_elections_serializer
@api_view(["POST"])
def do_vote(request):
                print(request.data)
                candidates=request.data["names"]
                candidates=candiates.objects.filter(name=candidates).first()
                candidates.number_of_votes=candidates.number_of_votes+1
                
                candidates.save()
                
                return Response("done")
@api_view(["POST"])
def create_unique_id(request):
        name=request.data.get("name")
        number_of_candidates=request.data.get("number_of_candidates")
        unique_id=generate_unique_id(name,number_of_candidates)
        return Response(unique_id)

def generate_unique_id(name: str, number: int) -> str:
    # Concatenate the name and number into a single string
    combined = f"{name}{number}"
    
    # Generate a SHA-256 hash of the combined string
    unique_id = hashlib.sha256(combined.encode()).hexdigest()
    
    # Optionally, truncate the hash to a desired length (e.g., first 10 characters)
    unique_id = unique_id[:10]
    
    return unique_id

# Example usage


                                

        
