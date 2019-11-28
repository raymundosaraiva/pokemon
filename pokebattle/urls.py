from django.urls import path

from . import views, engine

urlpatterns = [
    path('', views.battle, name='index'),
    path('battle', views.battle, name='battle'),
    path('mypokemon', views.my_pokemon, name='mypokemon'),
    path('stats', views.stats, name='stats'),
    path('about', views.about, name='about'),
    path('change_nickname', views.change_nickname, name='change_nickname'),
    path('loadgame', engine.load_game, name='loadgame'),
    path('pokemon/<int:pokemon_id>', views.pokemon, name='pokemon')
]
