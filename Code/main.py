import pygame
from menu import Menu
import subprocess
from guide import Guide
from contineu import Contineu
pygame.init()

def main_menu():
    menu = Menu()
    guide = None

    while True:
        menu.loop()
        if menu.pvp:
            menu.init_btn()
            file_to_run = "pvp.py"
            try:
                result = subprocess.run(["python", file_to_run], capture_output=True, text=True, check=True)
                print("Output:", result.stdout)
            except subprocess.CalledProcessError as e:
                print("Error:", e.stderr)
            if menu.pvp : del menu.pvp
            menu.pvp = None
            menu.running = True
            
        menu.loop()
        if menu.pve:
            menu.init_btn()
            file_to_run = "pve.py"
            try:
                result = subprocess.run(["python", file_to_run], capture_output=True, text=True, check=True)
                print("Output:", result.stdout)
            except subprocess.CalledProcessError as e:
                print("Error:", e.stderr)
            if menu.pve : del menu.pve
            menu.pve = None
            menu.running = True
                    
        if menu.guide:
            menu.init_btn()
            guide = Guide()
            guide.loop()
            if guide : del guide
            guide = None
            menu.running = True
        if menu._continue:
            menu.init_btn()
            try:
                file = open("save.txt", "r")
                board = convertStrToGrid(file.readlines()[0])
                file.close()
                contineu = Contineu(board)
                contineu.continue_game()
            except:
                menu.running = True
                menu.error_data = True
                continue 


main_menu()