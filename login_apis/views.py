from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializer import Users_models_serializer,CustomTokenObtainPairSerializer
from rest_framework.parsers import JSONParser
from .models import users
import bcrypt
from rest_framework_simplejwt.tokens import RefreshToken,UntypedToken,AccessToken
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.
class register_users(generics.ListCreateAPIView):
    queryset=users.objects.all()
    serializer_class=Users_models_serializer
@api_view(["POST"])
def register_user(request):
    if request.method == "POST":
        # Handle registration logic here
        data=users.objects.values()

        for user in data:
            print(request.data["username"])
            if user["username"]==request.data["username"]:
                return Response("user already exist")
        password=request.data.get("password")
        print("request",request.data)
        request.data["password"]=hash_password(password)
        print("request",request.data)
        print(request.data)
        serializer = Users_models_serializer(data=request.data)
        if serializer.is_valid():
            user_instance = serializer.save()  
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
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        print(user_id,user_id)
        user=users.objects.filter(id=user_id).first()
        if user:
            serializer=Users_models_serializer(user)
            return Response(serializer.data)
        else:
            return Response(12345)
    else:
        return Response({'error': 'Token not provided'}, status=400)
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
@api_view(["POST"])
def login(request):
    check_name=request.data.get("user_name")
    check_email=request.data.get("email")   
    plain_password=request.data.get("password") 
    user=users.objects.all().values()
    for user in user:
        if user["username"]==check_name:
            user=user
    print(user)
    hashed_password=user["password"]
    check_password=check_passwords(plain_password,hashed_password) 
    if check_password:
         return Response(user)
    else:
        return Response("false crediatilas")   
def hash_password(password: str) -> str:
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')
def check_passwords(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))


          
          
          











    