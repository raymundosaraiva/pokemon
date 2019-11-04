import json

jsonPath = './static/pokebattle/json/'
with open(jsonPath + 'pokemon_stats.json') as pokemon_stats, open(jsonPath + 'pokemon_types.json') as pokemon_types: 
	stats = json.load(pokemon_stats)
	types = json.load(pokemon_types)
	for s, t in zip(stats, types):
		pokemon_id = s['pokemon_id']
		name = s['pokemon_name']
		pokemon_type = t['type']
		attack = s['base_attack']
		defense = s['base_defense']
		stamina = s['base_stamina']


		