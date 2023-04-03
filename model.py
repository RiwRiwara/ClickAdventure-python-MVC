import random

class GameData:
    def __init__(self):
        self.name = "Jane"
        self.money = random.randint(150, 310) + 0
        self.health = 100
        self.point = 0
        self.atk = 0
        self.dur = 1
        self.isUseWeapon = False
        self.isUseDef = False

class Item:
    # Code = {0:weapon, 1:equipment, 9:extra}
    def __init__(self, name="", desc="", price=0, dur=1, atk=0, code=0,):
        self.code = code
        self.name = name
        self.desc = desc
        self.price = price
        self.dur = dur
        self.atk = atk
        self.isUse = False
    def __str__(self) -> str:
        return f"{self.name} {self.desc} {self.price} {self.dur} {self.atk} {self.code} "
    
class Room:
    def __init__(self, title="", content=[], damage=0, health=0, point = 0, money = 0) :
        self.title = title
        self.content = content
        self.damage = damage
        self.health = health
        self.point = point
        self.drops = []
        self.money = money
        self.baseHp = health