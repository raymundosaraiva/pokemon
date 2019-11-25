import datetime
import os
import json
# import requests

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse

from .models import *

USER_LOGIN = 'user_login'


def login(request):
    try:
        trainer_id = request.session[USER_LOGIN]
        trainer = Trainer.objects.get(id=trainer_id)
        print(f'Login from user: {trainer_id} at {datetime.datetime.now()}')
    except KeyError:
        print('Creating new user!')
        trainer = Trainer()
        trainer.save()
        request.session['user_login'] = trainer.id

    if not Pokemon.objects.all().exists():
        load_pokemon()

    return {'trainer': trainer,
            'my_pokemon': trainer.pokemon_collection.all()}

def remove_user(request):
    del request.session[USER_LOGIN]


@csrf_exempt
def change_nickname(request):
    trainer_id = request.session[USER_LOGIN]
    trainer = Trainer.objects.get(id=trainer_id)
    new_nickname = request.POST.get('nickname')
    if new_nickname:
        trainer.nickname = new_nickname
        trainer.save()
    return HttpResponse(new_nickname)


def load_pokemon():
    module_dir = os.path.dirname(__file__)
    json_path = module_dir + '/static/pokebattle/json/'
    with open(json_path + 'pokemon_stats.json') as pokemon_stats, \
        open(json_path + 'pokemon_types.json') as pokemon_types:
        stats = json.load(pokemon_stats)
        types = json.load(pokemon_types)
        for s, t in zip(stats, types):
            if 'form' not in s or 'Normal' in s['form']:
                pokemon_id = s['pokemon_id']
                name = fix_name(s['pokemon_name'])
                attack = s['base_attack']
                defense = s['base_defense']
                stamina = s['base_stamina']
                pokemon_type = t['type']
                # Save Pokemon
                pokemon = Pokemon.objects.get_or_create(pokemon_id=pokemon_id,
                                              name=name,
                                              attack=attack,
                                              defense=defense,
                                              stamina=stamina)
    pokemon_stats.close()
    pokemon_types.close()

def fix_name(name):
    if '♂' in name:
        name = name.replace('♂', 'm')
    elif '♀' in name:
        name = name.replace('♀', 'f')
    elif '’' in name:
        name = name.replace('’', '')
    elif '. ' in name:
        name = name.replace('. ', '-')
    return name


def check_url_exists(url):
    response = requests.head(url)
    return response.status_code == 200
