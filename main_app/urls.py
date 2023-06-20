from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('want_list/', views.want_list, name='want_list'),
    path('watch_list/', views.watch_list, name='watch_list'),
    path('detail/<str:result_id>/', views.detail, name='detail'),
    path('movies/<int:movie_id>/assoc_want_user/', views.assoc_want_user, name='assoc_want_user'),
    path('movies/<int:movie_id>/assoc_watched_user/', views.assoc_watched_user, name='assoc_watched_user'),
]