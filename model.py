import random

class GameData:
    def __init__(self):
        self.name = "Jane"
        self.money = random.randint(50, 310) + 5000
        self.health = 100
        self.point = 0
        self.atk = 0
        self.dur = 0
        self.isUse = False

class Item:
    # Code = {0:weapon, 1:equipment, 9:extra}
    def __init__(self, name="", desc="", price=0, dur=0, atk=0, code=0,):
        self.code = code
        self.name = name
        self.desc = desc
        self.price = price
        self.dur = dur
        self.atk = atk
        self.isUse = False
    def __str__(self) -> str:
        return f"{self.name} {self.desc} {self.price} {self.dur} {self.atk} {self.code}"
    
class Room:
    def __init__(self, title="", content="") :
        self.title = title
        self.content = content