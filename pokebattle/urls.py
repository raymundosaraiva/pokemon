from django.urls import path

from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='battle'),
    path('', views.index, name='mypokemon'),
    path('', views.index, name='stats'),
]
