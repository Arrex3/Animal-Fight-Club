from random import randint
class Animal:
    def __init__(self, name, emote="roars"):
        self.name = name
        self.emote = emote
        self.wins = 0

    def ROAR(self):
        print(f'{self.name} {self.emote}')

    def fights(self, opponent):
        winner = [self, opponent][randint(0, 1)]
        winner.wins += 1
        return winner


class Bird(Animal):
    def flap(self):
        print(f'{self.name} *fwap fwap fwap*')




lion = Animal("lion")
bear = Bird("bear")
duck = Bird("duck", "quacks")
while max([lion.wins, bear.wins, duck.wins]) < 100:

    duck.fights(bear)
    bear.fights(lion)
    lion.fights(duck)


sorted([lion, bear, duck], key=lambda a: a.wins, reverse=True)[0].ROAR()
print("record: ")
print(f'  lion: {lion.wins}')
print(f'  bear: {bear.wins}')
print(f'  duck: {duck.wins}')
