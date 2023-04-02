from model import  GameData, Item, Room
from view import WelcomeView, MenuView, InventoryView, ShopView, RoomView
import threading
import time
import tkinter.messagebox as messagebox

class UserController:
    def __init__(self, master):
        self.master = master
        self.gamedata = GameData()
        self.inventory = []
        self.rooms = [
            Room("Welcome to Sibenik" "This room have enemy with damage 5 Health 100")
        ]

        self.welcome_view = WelcomeView(self.master, self)
        self.menu_view = MenuView(self.master, self)
        self.inventory_view = InventoryView(self.master, self)
        self.shop_view = ShopView(self.master, self)
        self.room_view = RoomView(self.master, self)

        

        self.update_thread = threading.Thread(target=self.update_player_info, daemon=True)
        self.update_thread.start()
    
    def update_player_info(self):
        while True:
            self.menu_view.name_label.config(text=f"Player: {self.gamedata.name}")
            self.menu_view.health_label.config(text=f"Health: {self.gamedata.health}")
            self.menu_view.money_label.config(text=f"Money: {self.gamedata.money}")
            self.menu_view.point_label.config(text=f"Point: {self.gamedata.point}")
            self.menu_view.damage_label.config(text=f"Damage: {self.gamedata.atk} Defense: {self.gamedata.dur}")

            time.sleep(1)

    def addItem(self, item):
        item.price = int(item.price*0.6)
        self.inventory.append(item)

    def dropItem(self, index):
        del self.inventory[index]
        self.updateInv()

    def buyItem(self, item):
        if(self.gamedata.money >= item.price):
            if self.decidePopup("Confirm Action", "Are you sure?") :
                self.gamedata.money -= item.price
                self.addItem(item)
                self.popup("Complete" , f"You got a {item.name}!")
            else:
                pass
        else:
            self.popup("Caution" , "No enought money!")
    def updateInv(self):
        self.inventory_view.update(self.inventory)
    def popup(self, title, message):
        messagebox.showinfo(title, message)
    def decidePopup(self, title, message):
        confirmed = messagebox.askokcancel(title, message)
        return confirmed
    
    def useItem(self, name):
        item = self.getItem(name)
        if not item.isUse:
            if not self.gamedata.isUse:
                item.isUse = True
                self.gamedata.isUse = True
                self.gamedata.atk = item.atk
                self.inventory_view.use_button.config(text="Unused")
                
                self.popup("Message", f"You using {item.name}")
            else:
                self.popup("Caution", f"You already using item! Please unused it before and try again!")
        else:

            item.isUse = False
            self.gamedata.isUse = False
            self.gamedata.atk = 0
            self.inventory_view.use_button.config(text="Use")
            self.popup("Message", f"You unused {item.name}!")
    def sellItem(self, name):
        item = self.getItem(name)
        if item.isUse:
            self.popup("Caution", f"You already using item! Please unused it before and try again!")
        else:
            self.dropItem(self.getItemIndex(name))
            self.gamedata.money += item.price
            self.popup("Complete" , f"You sell a {item.name}!, Recieve {item.price}")
            self.inventory_view.selected_item_name.set('')
            self.inventory_view.selected_item_desc.set('')
            self.inventory_view.selected_item_price.set('')

    def getItem(self, name):
        for i in self.inventory:
            if i.name == name:
                return i
    def getItemIndex(self, name):
        n = 0
        for i in self.inventory:
            if i.name == name:
                return n
            n+=1

    def show_welcome_view(self):
        self.menu_view.frame.pack_forget()
        self.inventory_view.frame.pack_forget()
        self.shop_view.frame.pack_forget()
        self.room_view.frame.pack_forget()

        self.welcome_view.frame.pack()

    def show_menu_view(self):
        self.welcome_view.frame.pack_forget()

        self.menu_view.frame.pack()

    def show_inventory_view(self):
        self.updateInv()
        self.shop_view.frame.pack_forget()
        self.room_view.frame.pack_forget()

        self.inventory_view.frame.pack()

    def show_room1_view(self):
        self.shop_view.frame.pack_forget()
        self.inventory_view.frame.pack_forget()
        self.room_view.frame.pack()
    
    def show_room2_view(self):
        pass
    
    def show_room3_view(self):
        pass
    
    def show_room4_view(self):
        pass
    
    def show_shop_view(self):
        self.inventory_view.frame.pack_forget()
        self.room_view.frame.pack_forget()

        self.shop_view.frame.pack()