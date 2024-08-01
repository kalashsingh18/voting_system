from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializer import Userserializer,CustomTokenObtainPairSerializer
from rest_framework.parsers import JSONParser
from .models import users

from rest_framework_simplejwt.tokens import RefreshToken,UntypedToken,AccessToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class register_users(generics.ListCreateAPIView):
    queryset=users.objects.all()
    serializer_class=Userserializer
@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        # Handle registration logic here
        data=users.objects.values()

        for user in data:
            print(request.data["username"])
            if user["username"]==request.data["username"]:
                return Response("user already exist")
        serializer = Userserializer(data=request.data)
        
        if serializer.is_valid():
            user_instance = serializer.save()  # Save the user instance
            # Generate a token for the new user
            token = AccessToken.for_user(user_instance)
            refresh = RefreshToken.for_user(user_instance)  # Pass user_instance here
            return Response({
                'user': serializer.data,
                'token': str(token),
                'refresh_token':str(refresh)  # Convert token to string to make it JSON serializable
            })
        return Response(serializer.errors, status=400)
@api_view(["POST"])
def checktoken(request):
    
    print(request.headers)
    auth_header = request.headers.get('Authorization')

    print(auth_header)
    print(auth_header.startswith('Bearer '))
    if auth_header :
      print(auth_header)
      token = auth_header.split(' ')[1].strip()
      token=token[0:-1]
        
      try:
        access_token = AccessToken(token)
        

        user_id = access_token['user_id']
        print(user_id,user_id)
        user=users.objects.filter(id=user_id).first()
        print(type(user))
        if user:
            serializer=Userserializer(user)
            return Response(serializer.data)
        else:
            return Response(12345)
      except:
          pass

    else:
        return Response({'error': 'Token not provided'}, status=400)
    




          
          
          

# serializers.py






class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def login():
    pass