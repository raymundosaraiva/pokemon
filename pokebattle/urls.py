from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('battle', views.battle, name='battle'),
    path('mypokemon', views.my_pokemon, name='mypokemon'),
    path('stats', views.stats, name='stats'),
    path('about', views.about, name='about'),
    path('change_nickname', views.change_nickname, name='change_nickname'),
]
