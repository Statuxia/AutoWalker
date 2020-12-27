from keyboard import is_pressed, send, press
from time import sleep

key = "Num Lock"
mod = 0
block = False
print("""

 █████╗ ██╗   ██╗████████╗ █████╗  ██╗       ██╗ █████╗ ██╗     ██╗  ██╗███████╗██████╗ 
██╔══██╗██║   ██║╚══██╔══╝██╔══██╗ ██║  ██╗  ██║██╔══██╗██║     ██║ ██╔╝██╔════╝██╔══██╗
███████║██║   ██║   ██║   ██║  ██║ ╚██╗████╗██╔╝███████║██║     █████═╝ █████╗  ██████╔╝
██╔══██║██║   ██║   ██║   ██║  ██║  ████╔═████║ ██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║╚██████╔╝   ██║   ╚█████╔╝  ╚██╔╝ ╚██╔╝ ██║  ██║███████╗██║ ╚██╗███████╗██║  ██║
╚═╝  ╚═╝ ╚═════╝    ╚═╝    ╚════╝    ╚═╝   ╚═╝  ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                                                          
                                                                 ╔╗  ╔╗   ╔══╦══╦══╦═╦═╗
                                                          ╔══╦═╗╔╝╠═╗║╚╦╦╗║═╦╣╔╗║╔═╣║║║║
                                                          ║║║║╬╚╣╬║╩╣║╬║║║║╔╝║╚╝║╚╗║║║║║
                                                          ╚╩╩╩══╩═╩═╝╚═╬╗║╚╝ ╚═╗╠══╩╩═╩╝
                                                                       ╚═╝     ╚╝
""")
user_key = input("Напишите название кнопки для авто-бега (Num Lock по умолчанию): ")
if user_key != "":
    key = user_key
mod = int(input("Выберите способ бега (0 - только w, 1 - w + ctrl, 2 - w + ctrl + space): "))

while True:
    if is_pressed(key):
        if not block:
            if mod == 0:
                press("w")
            elif mod == 1:
                press("w")
                press("ctrl")
            elif mod == 2:
                press("w")
                press("ctrl")
                press("space")
            block = True
            sleep(.5)
        else:
            if mod == 0:
                send("w")
            elif mod == 1:
                send("w")
                send("ctrl")
            elif mod == 2:
                send("w")
                send("ctrl")
                send("space")
            block = False
            sleep(.5)