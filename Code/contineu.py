import pygame

class Contineu:
    def save(self):
        file = open("save.txt","w")
                       
        file.close()
    def continue_game(self):
            file = open("save.txt", "r")
            data = file.readlines()
            
            
    def convertStrToGrid(gridStr):
        parseGrid = []
        
        return parseGrid