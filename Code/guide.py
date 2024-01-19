import pygame
import sys
from menu import Button

class Guide:
    def __init__(self) -> None:
        self.running = True
        self.__screen_size = (1000, 800)
        self.__screen = pygame.display.set_mode(self.__screen_size[:2])
        pygame.display.set_caption("Gomoku")
    def __del__(self):
        pass
    def loop(self):
        while self.running:
            # set background
            bg = pygame.image.load("./image/bg.jpg")
            bg = pygame.transform.scale(bg, (1000, 800))
            self.__screen.blit(bg, (0, 0))
            # create object button
            MENU_BUTTON = Button(screen=self.__screen, pos=(500, 750-30),
                                     text_input="Menu", font=pygame.font.Font("./Dirtyboy.ttf", 50), base_color="#ffffff", hovering_color="#3399FF", size=(150, 60))
            #set title game
            font = pygame.font.Font("./Dirtyboy.ttf", 25)
            font_title = pygame.font.Font("./Dirtyboy.ttf", 50)
            font_intro_title = pygame.font.Font("./Dirtyboy.ttf", 25)
            font_intro = pygame.font.Font("./Dirtyboy.ttf", 25)
            #How to Play Caro
            line_title_1 = font_title.render("How to Play Caro", True, "#ffffff")
            line1 = font.render("In Caro, you need to have 5 X O symbols on the same 1 horizontal, vertical or diagonal row", True, "#ffffff")
            line2 = font.render("2 players or players with the machine will face each other in 1 match.",True, "#ffffff")
            line3 = font.render("The 2 sides will take turns hitting the umbrella and blocking each other to prevent the ....",True, "#ffffff")
            line_title_2 = font_title.render("Introduce", True, "#ffffff")
            intro1 = font_intro_title.render("Developer",True, "#ffffff")
            intro1_1 = font_intro.render("Nguyen Van Nhat",True, "#ffffff")
            #version
            intro2 = font_intro_title.render("Version ",True, "#ffffff")
            intro2_2 = font_intro.render("2.0",True, "#ffffff")
            #release
            intro3 = font_intro_title.render("Release ",True, "#ffffff")
            intro3_3 = font_intro.render("29 11 2023",True, "#ffffff")
            #engine
            intro4 = font_intro_title.render("Engine ",True, "#ffffff")
            intro4_4 = font_intro.render("Python, pygame",True, "#ffffff")
            #line
            self.__screen.blit(line_title_1,(44, 100 - 30))
            self.__screen.blit(line1,(44, 150 - 30))
            self.__screen.blit(line_title_2,(44, 200 - 30))
            self.__screen.blit(line2,(44, 250 - 30))
            self.__screen.blit(line3,(44, 300 - 30))
            #version
            self.__screen.blit(intro1,(44, 350 - 30))
            self.__screen.blit(intro1_1,(44, 400 - 30))
            self.__screen.blit(intro2,(44, 450 - 30))
            self.__screen.blit(intro2_2,(250, 450 - 30))
            #release
            self.__screen.blit(intro3,(44, 500 - 30))
            self.__screen.blit(intro3_3,(250, 500 - 30))
            #Engine
            self.__screen.blit(intro4,(44, 550 - 30))
            self.__screen.blit(intro4_4,(250, 550 - 30))
            # draw button
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            for button in [MENU_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update()
            # check vent
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.running = False
            pygame.display.update()

