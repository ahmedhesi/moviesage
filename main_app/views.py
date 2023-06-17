from django.shortcuts import render
import requests, os
import environ
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

def search(request):    
  url = f"https://imdb-api.com/en/API/SearchMovie/{os.environ['API_KEY']}/{request.POST['searchbar']}"
  data = requests.request("GET", url).json()
  return render(request, 'search.html', {
    'results': data['results']
  })

def result_detail(request, result_id):
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




  
  