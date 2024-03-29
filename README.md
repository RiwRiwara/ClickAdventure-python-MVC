﻿# ClickAdventure-python-MVC
- Python -> Tkinter, Threading
- Design Pattern -> MVC (Models-Views-Controller)

## Controller.py
คลาส UserController ใช้การจัดการสถานะของเกมและอินเทอร์เฟซผู้ใช้ โดยจะเริ่มต้นจะกำหนด ข้อมูลเกม(Ganedata) ห้อง(Room) และคุณสมบัติของห้อง รวมถึงมุมมอง(View)สำหรับแต่ละหน้าจอเกม ยินดีต้อนรับ(Welcome) เมนู(Menu) กระเป๋า(Inventory) ร้านค้า(Shop) และมุมมองห้อง(View)

Class ประกอบด้วยารจัดการกับการกระทำต่างๆ ของเกม เช่น การซื้อ(buy) การขาย(sell) และการใช้ไอเท็ม(UseItem) การวิ่ง(Run)และการต่อสู้(Fight)ในห้อง และการแสดงข้อความป๊อปอัป นอกจากนี้ยังมีวิธีการสลับระหว่างมุมมองเกมต่างๆ

และมีเธรดแยกต่างหาก (Threading)ใช้เพื่ออัปเดตข้อมูลผู้เล่น
```
    def end(self):
        ...
    def update_player_info(self):
        ...
    def addItem(self, item):
        ...
    def dropItem(self, index):
        ...
    def buyItem(self, item):
        ...
    def updateInv(self):
        ...
    def popup(self, title, message):
        ...
    def decidePopup(self, title, message):
        ...
    def useItem(self, name):
        ...
    def sellItem(self, name):
        ...
    def getItem(self, name):
        ...
    def getItemIndex(self, name):
        ...
    def setBtn(self, action):
        ...
    def run(self):
        ...
    def fight(self):
        ...
    def checkWin(self):
        ...
    def show_welcome_view(self):
        ...
    def show_menu_view(self):
        ...
    def show_inventory_view(self):
        ...
    def show_room1_view(self):
        ...
    def show_shop_view(self):
        ...
```
## model.py
class gamedata:
แสดงถึงข้อมูลเกมของผู้เล่น ชื่อผู้เล่น(Name) เงิน(Money) เลือด(Health) คะแนน(points) การโจมตี(atk) การป้องกัน(dur) และสถานะการใช้อาวุธและป้องกัน เงินเริ่มต้นด้วยค่าสุ่มระหว่าง 150 ถึง 310

class item:
คลาสนี้เป็นตัวแทนของไอเท็มในเกม ชื่อ(name) คำอธิบาย(desc) ราคา(price) ความทนทาน(dur) การโจมตี(atk) และรหัสที่แสดงถึงประเภทของไอเทม(code) ประเภทรายการคือ: อาวุธ (0), อุปกรณ์ (1) และพิเศษ (9) แต่ละรายการยังมีตัวแปรบูลีน isUse เพื่อแสดงว่ารายการนั้นกำลังถูกใช้งานอยู่หรือไม่

class room:
คลาสนี้เป็นตัวแทนของห้องต่างๆ ในเกม แต่ละห้องมีชื่อ(title) เนื้อหา(content) ความเสียหาย(damage)  เลือดมอนสเตอร์(health) คะแนน(point) (ได้รับจากการเอาชนะ) และเงิน (ได้รับจากการเอาชนะ) ห้องนี้ยังมีรายการของที่สามารถดรอปได้

## view.py
ประกอบด้วยหลาย class แต่ละคลาสแสดงถึงมุมมองที่แตกต่างกันของเกม:

WelcomeView: มุมมองเริ่มต้นของเกมที่ผู้เล่นป้อนชื่อและเริ่มเกม
MenuView: เมนูหลักของเกมที่ผู้เล่นสามารถเข้าถึงคุณสมบัติต่างๆ เช่น กระเป๋า ร้านค้า และห้องต่างๆ
InventoryView: มุมมองที่ผู้เล่นสามารถดูไอเท็มและใช้หรือขายได้
ShopView: มุมมองที่ผู้เล่นสามารถซื้อไอเทมได้
RoomView: มุมมองที่ผู้เล่นโต้ตอบกับห้องที่พวกเขาอยู่และเนื้อหาในห้อง
แต่ละมุมมองเชื่อมโยงกับคลาส Controller.py ที่จัดการตรรกะของเกมและอัปเดตมุมมองตามนั้น 

GUI สร้างขึ้นโดยใช้เฟรมและป้ายกำกับ และมีการเพิ่มปุ่มเพื่อให้ผู้เล่นสามารถโต้ตอบกับเกมได้ ข้อมูลเกมถูกจัดเก็บไว้ใน Instance ของคลาส GameData ที่ดึงมาจาก Controller.py 

## main.py

class App มีเมธอด __init__ ที่เริ่มต้นหน้าต่าง GUI และตั้งค่าคุณสมบัติต่างๆ เช่น width title และกำหนดว่าจะปรับขนาดได้หรือไม่ นอกจากนี้ยังสร้างอินสแตนซ์ของคลาส UserController   จาก controller.py และเรียกใช้เมธอด show_welcome_view() ซึ่งมีหน้าที่แสดงหน้า Welcome

คำสั่งเงื่อนไข __name__ == "__main__" ที่ด้านล่างของโค้ดจะตรวจสอบว่าสคริปต์ถูกรันโดยตรงหรือนำเข้าไปยังโมดูลอื่นหรือไม่ หากมีการเรียกใช้โดยตรง จะสร้างอินสแตนซ์ของคลาส App และเริ่มลูปหลัก GUI โดยใช้เมธอด mainloop() ของวัตถุ root ซึ่งเป็นอินสแตนซ์ของคลาส Tk() ลูปหลักนี้จะรับเหตุการณ์ของผู้ใช้และอัปเดต GUI ตามความจำเป็น
