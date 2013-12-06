import random

import messages

MAJOR_NPCS = {
  'ag': 'Angles Gator',
  'bf': 'Barry Fandling',
  'btf': 'Barret Falster',
  'pw': 'Playton Williams',
  'sf': 'Sherry Fandling',
  't': 'Troid',
  }

CAMPERS = {
  'bd': 'Brent Drago',
  'bl': 'Botany Lynn',
  'br': 'Bnola Rae',
  'bt': 'Boris Tortavich',
  'ct': 'Can Tabber',
  'fj': 'Freetus Jaunders',
  'gm': 'Gloobin Marfo',
  'gy': 'Gelliot Yabelor',
  'il': 'Illetia Dorfson',
  'jf': 'Jupiter Fargo',
  'kt': 'Kinser Talebearing',
  'nb': 'Nugget Beano',
  'nk': 'Niche Kaguya',
  'nt': 'Ninar Tetris',
  'pb': 'Pooder Bennet',
  'rb': 'Randy Buffet',
  'tn': 'Trinda Noober',
  'tv': 'Trinoba Vyder',
  'vt': 'Volga Toober',
  'yk': 'Yeldstat Krong',
  }

CAMPER_GENDER = {
  'bd': 'm',
  'bl': 'f',
  'br': 'f',
  'bt': 'm',
  'ct': 'm',
  'fj': 'm',
  'gm': 'm',
  'gy': 'm',
  'il': 'f',
  'jf': 'f',
  'kt': 'm',
  'nb': 'm',
  'nk': 'f',
  'nt': 'f',
  'pb': 'm',
  'rb': 'm',
  'tn': 'f',
  'tv': 'f',
  'vt': 'f',
  'yk': 'f',
  }

DISPO_COUNTER = {
  'pb': 0,
  'jf': 0,
  'rb': 0,
  'bl': 0,
  'bt': 0,
  'tn': 0,
  'fj': 0,
  'nt': 0,
  'gm': 0,
  'nk': 0,
  'bd': 0,
  'vt': 0,
  'kt': 0,
  'br': 0,
  'nb': 0,
  'yk': 0,
  'gy': 0,
  'il': 0,
  'ct': 0,
  'tv': 0,
}

def get_campers(gender=None):
  if gender:
    return [c for (c, g) in CAMPER_GENDER.items() if g == gender]
  else:
    return CAMPERS

def random_camper(gender=None):
  return random.choice(get_campers(gender))

def random_camper_sample(count, gender=None):
  return random.sample(get_campers(gender), 5)

def name(key):
  return CAMPERS.get(key) or MAJOR_NPCS[key]

def choice_list(people):
  names = (name(p) for p in people)
  choices = ('%d. %s' % (i + 1, name) for (i, name) in enumerate(names))
  return '\n\n'.join(choices)

def choose_person(people, message):
  message = message + choice_list(people) + messages.REQUEST_A_NUMBER
  while True:
    choice = raw_input(message)
    try:
      return people[int(choice) - 1]
    except:
      print messages.BAD_NUMBER_MESSAGE % len(people)
