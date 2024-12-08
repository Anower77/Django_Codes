from django.db import models

class Musician(models.Model):
    # id_pk = models.IntegerField(primary_key = True) 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    instrument_type = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return self.album_name
