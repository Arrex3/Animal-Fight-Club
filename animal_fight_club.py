from random import choice, randint, sample

from models import Animal, Referee


ANIMALS = [
    "lion",
    "bear",
    "bluebird",
    "duck",
    "mouse",
    "elephant",
    "Stuart",
    "pangolin",
    "armadillo",
    "newt",
    "wolverine",
    "komodo dragon",
    "basilisk",
    "unicorn",
    "garter snake",
    "koala",
]

EMOTES = [
    "roar",
    "growl",
    "hiss",
    "ffft",
    "hoooah",
    "huzzah",
    "squeak",
    "plap",
    "groan",
    "zzz",
    "keekee",
    "caw",
    "honk",
]


ref = Referee("Telemachus")
for animal in sample(ANIMALS, randint(3, 10)):
    combatant = Animal(animal, choice(EMOTES))
    ref.add_combatant(combatant)

ref.fight()
