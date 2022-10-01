from models.fighter import Fighter


class Animal(Fighter):
    """An animal fights."""

    def cheer(self) -> str:
        return f"{self.emote.upper()}!!!"
