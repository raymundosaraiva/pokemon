import random

from django.shortcuts import render
from django.forms.models import model_to_dict

from .controller import *


@csrf_exempt
def load_game(request):
    trainer_id = request.session[USER_LOGIN]
    trainer = Trainer.objects.get(id=trainer_id)
    # Get Not Started or In Progress Games or Create a New one
    game = Game.objects.filter(trainer=trainer, status__lt=2)
    context = {'trainer': trainer}

    if not game.exists():
        game = Game(trainer=trainer, mode=0, status=0)
        game.save()
        # Create Battles
        for num in range(NUM_BATTLES):
            # Get Random Pokemon
            game.pokemon_trainer.add(Pokemon.objects.order_by('?')[:1].get())
            pokemon_pc = Pokemon.objects.order_by('?')[:1].get()
            Battle(num=num+1,
                   type=random.choice([1, 2]),
                   game=game,
                   pokemon_pc=pokemon_pc).save()
    else:
        game = game.get()

    if not game.mode:
        mode = request.POST.get('mode')
        if not mode:
            return init(request, context)
        game.mode = mode
        game.status = 1
        game.current_battle = 1
        game.save()

    battle = Battle.objects.get(game=game, num=game.current_battle)

    if not battle.pokemon_trainer:
        pokemon_id = request.POST.get('pokemon')
        if not pokemon_id and battle.num != NUM_BATTLES:
            return choose_pokemon(request, context, game)
        if battle.num == NUM_BATTLES:
            pokemon = game.pokemon_trainer.get()
        else:
            pokemon = Pokemon.objects.get(pokemon_id=pokemon_id)
        battle.pokemon_trainer = pokemon
        battle.save()
        game.pokemon_trainer.remove(pokemon)

    if not battle.result:
        move = request.POST.get('move')
        if not move:
            return start_battle(request, context, battle)
        else:
            return end_battle(request, context, game, battle)

    # In case of Error
    return render(request, 'pokebattle/404.html')


def choose_pokemon(request, context, game):
    battle = Battle.objects.get(game=game, num=game.current_battle)
    pokemon = [get_pokemon_and_img_url(pokemon) for pokemon in game.pokemon_trainer.all()]
    # If Level is #1 Easy
    pokemon_pc = get_pokemon_and_img_url(battle.pokemon_pc) if game.mode == 1 else None
    context.update({'battle': BATTLE_NUM_DICT[battle.num],
                    'type': BATTLE_TYPE_DICT[battle.type],
                    'pokemon': pokemon,
                    'colsize': int(12/len(pokemon)),
                    'pokemon_pc': pokemon_pc
                    })
    return render(request, 'pokebattle/game_choose_pokemon.html', context)


def init(request, context):
    return render(request, 'pokebattle/game_init.html', context)


def start_battle(request, context, battle):
    pokemon_defense = battle.pokemon_pc if battle.type == 1 else battle.pokemon_trainer
    pokemon_attack = battle.pokemon_trainer if battle.type == 1 else battle.pokemon_pc
    context.update({'battle': BATTLE_NUM_DICT[battle.num],
                    'type': BATTLE_TYPE_DICT[battle.type],
                    'pokemon_defense': get_pokemon_and_img_url(pokemon_defense, is_back=True),
                    'pokemon_attack': get_pokemon_and_img_url(pokemon_attack),
                    })
    return render(request, 'pokebattle/game_start.html', context)


def end_battle(request, context, game, battle):
    pokemon_defense = battle.pokemon_pc if battle.type == 1 else battle.pokemon_trainer
    pokemon_attack = battle.pokemon_trainer if battle.type == 1 else battle.pokemon_pc
    battle.result = get_result(battle)
    battle.save()
    if battle.num == NUM_BATTLES:
        game.final_result = get_final_result(game)
        game.status = 2  # Completed
    else:
        game.current_battle += 1
    game.save()
    context.update({'battle': BATTLE_NUM_DICT[battle.num],
                    'type': BATTLE_TYPE_DICT[battle.type],
                    'type_pc': BATTLE_TYPE_DICT[1 if battle.type == 2 else 2],
                    'pokemon_defense': get_pokemon_and_img_url(pokemon_defense, is_back=True),
                    'pokemon_attack': get_pokemon_and_img_url(pokemon_attack),
                    'result': FINAL_RESULT_DICT.get(battle.result),
                    'next': not battle.num == NUM_BATTLES,
                    })
    return render(request, 'pokebattle/game_end.html', context)


def get_pokemon_and_img_url(pokemon, is_back=None):
    pokemon = model_to_dict(pokemon)
    url = IMG_PATH + (BACK if is_back else '') + pokemon['name'].lower() + GIF
    pokemon.update({'url': url})
    return pokemon


def get_result(battle):
    type = battle.type
    pokemon_trainer = battle.pokemon_trainer
    pokemon_pc = battle.pokemon_pc
    if type == 1:  # Attack
        result = pokemon_trainer.attack - pokemon_pc.defense
    else:  # Defense
        result = pokemon_trainer.defense - pokemon_pc.attack

    if not result:
        return 2  # Tie
    elif result > 0:
        return 3  # Win
    else:
        return 1  # Lost


def get_final_result(game):
    battles = Battle.objects.filter(game=game).all()
    return 2  # TODO