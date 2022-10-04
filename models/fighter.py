from random import randint


class Fighter:
    """A fighter fights."""

    def __init__(self, name, emote="huzzah"):
        self.name = name
        self.emote = emote
        self.wins = 0

    def cheer(self) -> str:
        return f"{self.emote.title()}!"

    def fights(self, opponent):
        """Fight against an opponent!"""
        winner = [self, opponent][randint(0, 1)]
        winner.wins += 1
        return winner
