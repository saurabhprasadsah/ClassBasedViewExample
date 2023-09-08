from django.db import models

class Employee(models.Model):
    id =models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    dsg=models.CharField(max_length=20)
    phone=models.CharField(max_length=15,default="")   
    salary=models.IntegerField()
    city=models.CharField(max_length=20,default="",null=True, blank=True)
    state=models.CharField(max_length=20,default="",null=True, blank=True)

