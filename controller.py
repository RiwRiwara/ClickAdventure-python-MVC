from model import  GameData, Item
from view import WelcomeView, MenuView, InventoryView, ShopView
import threading
import time
import tkinter.messagebox as messagebox

class UserController:
    def __init__(self, master):
        self.master = master
        self.gamedata = GameData()
        self.inventory = []

        self.welcome_view = WelcomeView(self.master, self)
        self.menu_view = MenuView(self.master, self)
        self.inventory_view = InventoryView(self.master, self)
        self.shop_view = ShopView(self.master, self)

        

        self.update_thread = threading.Thread(target=self.update_player_info, daemon=True)
        self.update_thread.start()
    
    def update_player_info(self):
        while True:
            self.menu_view.name_label.config(text=f"Player: {self.gamedata.name}")
            self.menu_view.health_label.config(text=f"Health: {self.gamedata.health}")
            self.menu_view.money_label.config(text=f"Money: {self.gamedata.money}")
            self.menu_view.point_label.config(text=f"Point: {self.gamedata.point}")

            time.sleep(1)

    def addItem(self, item):
        self.inventory.append(item)

    def dropItem(self, index):
        del self.inventory[index]
        self.updateInv()

    def buyItem(self, item):
        if(self.gamedata.money >= item.price):
            self.gamedata.money -= item.price
            self.addItem(item)
        else:
            self.popup("Caution" , "No enought money!")
    def updateInv(self):
        self.inventory_view.update(self.inventory)
    def popup(self, title, message):
        messagebox.showinfo(title, message)
    def show_welcome_view(self):
        self.menu_view.frame.pack_forget()
        self.inventory_view.frame.pack_forget()
        self.shop_view.frame.pack_forget()

        self.welcome_view.frame.pack()

    def show_menu_view(self):
        self.welcome_view.frame.pack_forget()

        self.menu_view.frame.pack()

    def show_inventory_view(self):
        self.updateInv()
        self.shop_view.frame.pack_forget()

        self.inventory_view.frame.pack()

    def show_room1_view(self):
        pass
    
    def show_room2_view(self):
        pass
    
    def show_room3_view(self):
        pass
    
    def show_room4_view(self):
        pass
    
    def show_shop_view(self):
        self.inventory_view.frame.pack_forget()

        self.shop_view.frame.pack()