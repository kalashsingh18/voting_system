from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
   path("register",views.register_user,name="register"),
   path("check_token",views.checktoken,name="check_token"),
   path("login",views.login,name="login"),
]