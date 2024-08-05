from django.db import models

# Create your models here.
class users(models.Model):
    username=models.CharField(max_length=1234)
    email=models.EmailField()
    password=models.TextField(max_length=13456)