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
    trainer = context.get('trainer')
    pokemon = [get_pokemon_and_img_url(pokemon) for pokemon in trainer.pokemon_collection.all()]
    context.update({'my_pokemon': pokemon,
                    'colsize': int(12 / len(pokemon)) if len(pokemon) > 0 else 12,
                    'pokemon_count': len(pokemon)})
    return render(request, 'pokebattle/my_pokemon.html', context)

def pokemon(request, pokemon_id):
    context = login(request)
    pokemon = Pokemon.objects.get(pokemon_id=pokemon_id)
    pokemon = get_pokemon_and_img_url(pokemon)
    context.update({'pokemon': pokemon})
    return render(request, 'pokebattle/pokemon_details.html', context)

def stats(request):
    context = login(request)
    return render(request, 'pokebattle/stats.html', context)


def about(request):
    context = login(request)
    return render(request, 'pokebattle/about.html', context)
