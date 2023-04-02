
from tkinter import *
from controller import UserController

class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x800")
        self.master.resizable(False, False)
        self.master.title("My Game") 
        self.controller = UserController(self.master)
        self.controller.show_welcome_view()
    
if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
