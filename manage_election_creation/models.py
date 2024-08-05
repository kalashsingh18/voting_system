from django.db import models
# from ..login_apis import models
# Create your models here.
from login_apis import models as mdd
class candiates(models.Model):
       name=models.CharField(max_length=12345678)
       postion=models.CharField(max_length=1234356478)
       number_of_votes=models.IntegerField(default=0)

class create_elections(models.Model):
    organizer=models.ForeignKey(mdd.users,on_delete=models.CASCADE)
    title=models.CharField(max_length=12345678,default="")
    number_of_candidates=models.IntegerField(default=0)
