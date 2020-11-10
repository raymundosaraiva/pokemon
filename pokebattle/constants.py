NUM_BATTLES = 3
ANONYMOUS = 'Anonymous'
GAME_MODE = ((0, 'Not Defined'), (1, 'Easy'), (2, 'Medium'), (3, 'Hard'))
GAME_STATUS = ((0, 'Not Started'), (1, 'In Progress'), (2, 'Completed'))
FINAL_RESULT = ((0, 'Not Defined'), (1, 'Lost'), (2, 'Tie'), (3, 'Won'))
BATTLE_TYPE = ((1, 'Attack'), (2, 'Defense'))
BATTLE_NUM = ((1, 'First'), (2, 'Second'), (3, 'Third'))

BATTLE_TYPE_DICT = dict(BATTLE_TYPE)
GAME_MODE_DICT = dict(GAME_MODE)
BATTLE_NUM_DICT = dict(BATTLE_NUM)
FINAL_RESULT_DICT = dict(FINAL_RESULT)
# https://img.pokemondb.net/sprites/black-white/anim/normal/bulbasaur.gif
# https://img.pokemondb.net/sprites/black-white/anim/back-normal/bulbasaur.gif
IMG_PATH = 'https://img.pokemondb.net/sprites/black-white/anim/'
THUMB_IMG_PATH = 'http://www.pokestadium.com/assets/img/sprites/misc/trozei/'
BACK = 'back-normal/'
GIF = '.gif'