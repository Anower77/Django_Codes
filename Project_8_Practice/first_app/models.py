from django.db import models

# Create your models here. (first make this table then do comment [makemigrations] [migrate])
class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key = True)
    address= models.TextField()
    father_name = models.TextField(default="Node")