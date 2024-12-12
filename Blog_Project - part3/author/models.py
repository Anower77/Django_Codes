from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField()
    phone_no = models.IntegerField(max_length=12)
    
    def __str__(self):
        return self.name
    
    
    
    
    
    
    
    
    
    
    
    