from django.shortcuts import render
from .serializer import Candidatesserializer,Create_elections_serializer
import base64
import json
from rest_framework.response import Response
from .models import candiates
from rest_framework.decorators import api_view
from .models import candiates,create_elections
from rest_framework import generics
# from .models import create_elections,candiates
from .models import create_elections as ce
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
                candidates=candiates.object.filter(name=candidates).first()
                candidates.number_of_votes=candidates.number_of_votes+1
                
                candidates.save()
                
                return Response("done")
@api_view(["POST"])
def create_unique_id(request):
        name=request.data.get("name")
        
        number_of_candidates=request.data.get("number_of_candidates")
        unique_id=generate_unique_id(name,number_of_candidates)
        id=type(unique_id)
        return Response(unique_id,status=200)
@api_view(["POST"])
def select_election(request):
    # Extract the unique_id from the request data
    unique_id=request.data.get("unique_id")
    if unique_id:
           unique_id=decode_unique_id(unique_id)
           election=ce.objects.all().values()
           return Response(election)
    
@api_view(["GET"])
def details_of_election(request):
       election_name=request.dta.get("election_name")
       number_of_candidates=request.data.get("number_of_candidates")
       
def generate_unique_id(name: str, number: int) -> str:
    combined = f"{name}:{number}"
    
    # Encode the combined string to Base64
    encoded_bytes = base64.urlsafe_b64encode(combined.encode('utf-8'))
    encoded_str = encoded_bytes.decode('utf-8')
    
    return encoded_str

def decode_unique_id(encoded_str: str) :
    # Decode the Base64 string back to the original combined string
    decoded_bytes = base64.urlsafe_b64decode(encoded_str.encode('utf-8'))
    decoded_str = decoded_bytes.decode('utf-8')
    
    # Split the combined string to retrieve name and number
    name, number = decoded_str.split(':')
    
    return name, int(number)
# Example usage


                                

        
