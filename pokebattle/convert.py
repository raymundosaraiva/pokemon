import json

jsonPath = './static/pokebattle/json/'
with open(jsonPath + 'pokemon_stats.json') as pokemon_stats, open(jsonPath + 'pokemon_types.json') as pokemon_types:
    stats = json.load(pokemon_stats)
    types = json.load(pokemon_types)
    poke_list = []
    for s, t in zip(stats, types):
        form = s.get('form')

        if not form or (form and form == "Normal"):
            pokemon = {
                "pokemon_id": s['pokemon_id'],
                "name": s['pokemon_name'],
                "pokemon_type": t['type'],
                "attack": s['base_attack'],
                "defense": s['base_defense'],
                "stamina": s['base_stamina']
            }
            poke_list.append(pokemon)

    print(len(poke_list))

with open(jsonPath + "poke_file.json", "w") as write_file:
    json.dump(poke_list, write_file, indent=4)
