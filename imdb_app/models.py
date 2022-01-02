from django.db import models


# Create your models here.

class Actor(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    dob = models.DateField()
    bio = models.CharField(max_length=200)
   
    def __str__(self):
        return self.name

class Producer(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    dob = models.DateField()
    bio = models.CharField(max_length=200) 
   
    def __str__(self):
        return self.name

 
class Movie(models.Model):
    name = models.CharField(max_length=200) 
    year_of_release = models.CharField(max_length=4)
    plot = models.TextField()
    poster = models.ImageField(default=None, upload_to='poster_pics')
    actor = models.ManyToManyField(Actor)
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

