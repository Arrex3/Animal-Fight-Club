#!/usr/bin/env python

from operator import attrgetter
from random import choice
from typing import List, Tuple

from models.fighter import Fighter


CORNERS = [
    "left",
    "right",
    "far",
    "near",
    "top-left",
    "top-right",
    "top-middle",
    "left-middle",
    "right-middle",
    "bottom-right",
    "bottom-left",
    "bottom-middle",
    "kitty",
]

HYPE = [
    "all the way from Saskatoon",
    "still wearing their bathrobe",
    "with a face only their mother could love",
    "trembling like a newborn deer",
    "looking like they don't know where they are",
    "texting their buddies back home",
    "building a card tower",
    "brushing their teeth with steel wool",
    "with rage in their eyes",
    "like they've got somethin' to prove",
]


class Referee:
    """Refs a fight amongst a group."""

    def __init__(self, name: str) -> None:
        self.name = name
        self.combatant_list = []

    def add_combatant(self, combatant: Fighter) -> None:
        """Add a fighter to this round."""
        self.combatant_list.append(combatant)

    def announce(self) -> None:
        """Announce the combatants."""
        not_first = False
        print(
            "We've got a great fight for you today folks,"
            f" just look at these {len(self.combatant_list)} fighters..."
        )
        for combatant in self.combatant_list:
            print(
                f"{f'And in' if not_first else 'In'} the {choice(CORNERS)} corner,"
                f" {choice(HYPE)}, {combatant.name.upper()}!"
            )
            not_first = True

        print("Let's get READY TO RUMBLE!!!\n")

    def _get_pairs(self) -> List[Tuple[Fighter, Fighter]]:
        """Pair the combatants up, probably for a round."""
        pairings = list(zip(self.combatant_list, self.combatant_list[1:]))
        pairings.append((self.combatant_list[-1], self.combatant_list[0]))

        return pairings

    def fight(self, to: int = 100) -> Fighter:
        """Start and complete the fight, returning the winner."""
        self.announce()
        print(f"All right everyone, i want a good clean fight. First to {to}!\n")
        while max(combatant.wins for combatant in self.combatant_list) < to:
            pairings = self._get_pairs()
            for first, second in pairings:
                first.fights(second)

        winner = sorted(self.combatant_list, key=attrgetter("wins"), reverse=True)[0]
        print(f"{winner.name} wins!")
        print(f"{winner.name}: {winner.cheer()}")
        return winner

    def reset(self) -> None:
        """Set all combatants' wins back to 0 and clear the list."""
        for combatant in self.combatant_list:
            combatant.wins = 0

        self.combatant_list = []
