import datetime
import os
import json
# import requests

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import HttpResponse
from django.forms.models import model_to_dict

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
    return {'trainer': trainer}


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

def get_pokemon_and_img_url(pokemon, is_back=None):
    pokemon = model_to_dict(pokemon)
    url = IMG_PATH + (BACK if is_back else '') + pokemon['name'].lower() + GIF
    pokemon.update({'url': url})
    return pokemon

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



### Sort

def pokemon_sort_att(Pokemon):
    return Pokemon.attack

sa_pok = sorted(Pokemon, key=pokemon_sort_att)

def pokemon_sort_def(Pokemon):
    return Pokemon.defense

sd_pok = sorted(Pokemon, key=pokemon_sort_def)

def pokemon_sort_sta(Pokemon):
    return Pokemon.stamina

ss_pok = sorted(Pokemon, key=pokemon_sort_sta)


 
### Quick Sort

def particionar(lista, inicio, fim, atributo):
    pivo = lista[fim]
    inferior = inicio-1
    superior = fim

    valor_pivo = 0
    valor_inferior = 0
    valor_superior = 0

    

    ok = 0
    while not ok:

        while not ok:
            inferior = inferior + 1

            if(atributo == 1):
                valor_inferior = lista[inferior].get_attack()
                valor_superior = lista[superior].get_attack()
                valor_pivo = lista[fim].get_attack()
            elif(atributo == 2):
                valor_inferior = lista[inferior].get_defense()
                valor_superior = lista[superior].get_defense()
                valor_pivo = lista[fim].get_defense()
            else:
                valor_inferior = lista[inferior].get_stamina()
                valor_superior = lista[superior].get_stamina()
                valor_pivo = lista[fim].get_stamina()



            if inferior == superior:
                ok = 1
                break

            if valor_inferior > valor_pivo:
                lista[superior] = lista[inferior]
                break

        while not ok:
            superior = superior-1

            if(atributo == 1):
                valor_inferior = lista[inferior].get_attack()
                valor_superior = lista[superior].get_attack()
                valor_pivo = lista[fim].get_attack()
            elif(atributo == 2):
                valor_inferior = lista[inferior].get_defense()
                valor_superior = lista[superior].get_defense()
                valor_pivo = lista[fim].get_defense()
            else:
                valor_inferior = lista[inferior].get_stamina()
                valor_superior = lista[superior].get_stamina()
                valor_pivo = lista[fim].get_stamina()

            if superior == inferior:
                ok = 1
                break

            if valor_superior < valor_pivo:
                lista[inferior] = lista[superior]
                break

    lista[superior] = pivo
    return superior

def quicksort(lista, inicio, fim, atributo):
    if inicio < fim:
        split = particionar(lista, inicio, fim, atributo)
        quicksort(lista, inicio, split-1, atributo)
        quicksort(lista, split+1, fim, atributo)
    else:
        return



sa_pok = quicksort(lista1,0,len(lista1)-1,1)

sd_pok = quicksort(lista2,0,len(lista2)-1,2)

ss_pok = quicksort(lista3,0,len(lista3)-1,3)

