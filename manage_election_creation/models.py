from django.db import models
# from ..login_apis import models
# Create your models here.
from login_apis import models as mdd

class create_elections(models.Model):
    organizer=models.ForeignKey(mdd.users,on_delete=models.CASCADE)
    title=models.CharField(max_length=12345678,default="")
    number_of_candidates=models.IntegerField(default=0)

class candiates(models.Model):
       name=models.CharField(max_length=12345678,default="None")
       postion=models.CharField(max_length=1234356478,default=12)
       number_of_votes=models.IntegerField(default=0)
       belong_to=models.ForeignKey(create_elections,on_delete=models.CASCADE,default=1)