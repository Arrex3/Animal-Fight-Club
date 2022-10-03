from random import choice, randint, sample

from data import ANIMALS, EMOTES
from models import Animal, Referee


ref = Referee("Telemachus")
for animal in sample(ANIMALS, randint(3, 10)):
    combatant = Animal(animal, choice(EMOTES))
    ref.add_combatant(combatant)

ref.fight()
