from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.



class Movie(models.Model):
  api_id = models.CharField(max_length=250)
  image = models.CharField(max_length=250)
  full_title = models.CharField(max_length=250)
  release_date = models.CharField(max_length=250)
  runtime_str = models.CharField(max_length=250)
  director = models.CharField(max_length=250)
  plot = models.CharField(max_length=250)
  stars = models.TextField(max_length=250)
  wanters = models.ManyToManyField(User, related_name='wanters_set' )
  watchers = models.ManyToManyField(User, related_name='watchers_set' )
  
  def __str__(self):
    return f'{self.full_title} ({self.id})'
    
class Review(models.Model):
  content = models.CharField(max_length=250, default='')
  rating = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(1)])
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

  
