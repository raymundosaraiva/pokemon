from django.shortcuts import render

from .controller import *


def index(request):
    context = login(request)
    return render(request, 'pokebattle/base.html', context)


def battle(request):
    context = login(request)
    return render(request, 'pokebattle/battle.html', context)


def my_pokemon(request):
    context = login(request)
    return render(request, 'pokebattle/my_pokemon.html', context)


def stats(request):
    context = login(request)
    return render(request, 'pokebattle/stats.html', context)


def about(request):
    context = login(request)
    return render(request, 'pokebattle/about.html', context)