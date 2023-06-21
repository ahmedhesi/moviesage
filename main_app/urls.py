from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('want_list/', views.want_list, name='want_list'),
    path('watch_list/', views.watch_list, name='watch_list'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('detail/<str:result_id>/', views.result_detail, name='result_detail'),
    path('movies/<int:movie_id>/assoc_want_user/', views.assoc_want_user, name='assoc_want_user'),
    path('movies/<int:movie_id>/assoc_watched_user/', views.assoc_watched_user, name='assoc_watched_user'),
    path('movies/<int:movie_id>/unassoc_want_user/', views.unassoc_want_user, name='unassoc_want_user'),
    path('movies/<int:movie_id>/unassoc_watched_user/', views.unassoc_watched_user, name='unassoc_watched_user'),
    path('accounts/signup/', views.signup, name='signup'),
]
    