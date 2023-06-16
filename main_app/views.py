from django.shortcuts import render
import requests, os
import environ
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
  #https://imdb-api.com/en/API/SearchMovie/k_4i13c7ul/inception%202010
  response = requests.request("GET", url)
  print(url)
  