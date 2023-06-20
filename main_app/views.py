import requests, os, environ
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Movie
environ.Env()
environ.Env.read_env()

# Create your views here.

# Define the home view
def home(request):
  # Include an .html file extension - unlike when rendering EJS templates
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

@login_required
def want_list(request):
  movies = Movie.objects.filter(user=request.user)
  # Another query
  # movies = request.user.cat_set.all()
  return render(request, 'want_watch_list.html', {
    'movies': movies
  })

@login_required
def watch_list(request):
  movies = Movie.objects.filter(user=request.user)
  # Another query
  # movies = request.user.movies_set.all()
  return render(request, 'watched_list.html', {
    'movies': movies
  })


def search(request):    
  url = f"https://imdb-api.com/en/API/SearchMovie/{os.environ['API_KEY']}/{request.POST['searchbar']}"
  data = requests.request("GET", url).json()
  return render(request, 'search.html', {
    'results': data['results']
  })

def detail(request, result_id):
  try:
    movie = Movie.objects.get(api_id=result_id)
    return render(request, 'movies/detail.html', {'movie': movie})
  except Movie.DoesNotExist:
    url = f"https://imdb-api.com/en/API/Title/{os.environ['API_KEY']}/{result_id}"
    data = requests.request("GET", url).json()
    print(data)
    new_movie = {
      'api_id': data['id'],
      'image': data['image'],
      'full_title': data['fullTitle'],
      'release_date': data['releaseDate'],
      'runtime_str': data['runtimeStr'],
      'director': data['directors'],
      'plot': data['plot'],
      'stars': data['stars']
    }
    movie = Movie.objects.create(**new_movie)
    movie.save()
    return render(request, 'movies/detail.html', {'movie': movie})




  
  