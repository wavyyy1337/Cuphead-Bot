import keyboard
import os
import time
import sys


os.system("@echo off")
os.system("color a")
os.system("cls")
os.system("title Bot made by cyberhure.#0001")
print("----------------")
print("Cuphead Bot!")
print("----------------")
print("Press F10 to Stop the Bot!, may not work!")
print("Press X to Start!")


while True:


    time.sleep(0.001)
    if keyboard.is_pressed("x"): # Change the Key if u want.
        while True:
            time.sleep(0.01)
            keyboard.press("r") # CHANGE TO YOUR SHOOT KEY!




    if keyboard.is_pressed("F10"):
        break
        os.system("cls")
        sys.exit("Bye!")


