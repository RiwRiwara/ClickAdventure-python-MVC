import random

class GameData:
    def __init__(self):
        self.name = "Jane"
        self.money = random.randint(50, 310) + 5000
        self.health = 100
        self.point = 0

class Item:
    def __init__(self, name="", desc="", price=0, dur=0, atk=0, code=""):
        self.code = code
        self.name = name
        self.desc = desc
        self.price = price
        self.dur = dur
        self.atk = atk
    def __str__(self) -> str:
        return f"{self.name} {self.desc} {self.price} {self.dur} {self.atk} {self.code}"
    