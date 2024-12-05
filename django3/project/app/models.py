from django.db import models

# Create your models here.
class Value(models.Model):
    Name=models.CharField(max_length=30,default='')
    Class=models.CharField(max_length=30,default='')
    Section=models.CharField(max_length=30,default='')
    Rollno=models.CharField(max_length=30,default='')

  
