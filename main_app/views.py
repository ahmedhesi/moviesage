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
 return render(request, 'home.html')


def about(request):
  return render(request, 'about.html')

@login_required
def want_list(request):
  movies = Movie.objects.filter(wanters=request.user)
  print(movies)
  return render(request, 'want_list.html', {
    'movies': movies
  })

@login_required
def watch_list(request):
  movies = Movie.objects.filter(watchers=request.user)
  # Another query
  # movies = request.user.movies_set.all()
  return render(request, 'watch_list.html', {
    'movies': movies
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


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
  
def assoc_want_user(request, movie_id):
   Movie.objects.get(id=movie_id).wanters_set.add(request.user.id)
   return redirect('want_list')

def unassoc_want_user(request, movie_id):
  Movie.objects.get(id=movie_id).wanters_set.remove(request.user.id)
  return redirect('want_list')

def assoc_watched_user(request, movie_id):
   Movie.objects.get(id=movie_id).watchers_set.add(request.user.id)
   return redirect('watch_list')

def unassoc_watched_user(request, movie_id):
  Movie.objects.get(id=movie_id).watchers_set.remove(request.user.id)
  return redirect('watch_list')



  
  