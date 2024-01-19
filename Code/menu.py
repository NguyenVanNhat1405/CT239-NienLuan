import pygame
import sys


class Menu:
    def __init__(self) -> None:
        self.running = True
        self.__screen_size = (1000, 800)
        self.__screen = pygame.display.set_mode(self.__screen_size[:2])
        self.pvp = False
        self.pve = False
        self.custom = False
        self._continue = False
        self.guide = False
        self.quit = False
        self.error_data = False
        self.time_press_btn = 0
        pygame.display.set_caption("Gomoku")

    def init_btn(self):
        self.pvp = False
        self.pve = False
        self.custom = False
        self._continue = False
        self.guide = False
        self.quit = False
    def draw_warning_continue(self):
         font = pygame.font.Font("Dirtyboy.ttf", 24) 
         text = font.render("You dont have data!", True, "white")
         text_rect = text.get_rect(center=(500, 750))
         self.__screen.blit(text, text_rect)
    def loop(self):
        clock = pygame.time.Clock()
        #time count game
        current_time = 0
        while self.running:
            # set background
            bg = pygame.image.load("./image/bg.jpg")
            bg = pygame.transform.scale(bg, (1000, 800))
            self.__screen.blit(bg, (0, 0))
            # create object button
            PVP_BUTTON = Button(screen=self.__screen, pos=(500, 300 - 30),
                                 text_input="Play With Player", font=pygame.font.Font("Dirtyboy.ttf", 50), base_color="#ffffff", hovering_color="#3399FF", size=(350, 60),)
            PVE_BUTTON = Button(screen=self.__screen, pos=(500, 400 - 30),
                                   text_input="Play With AI", font=pygame.font.Font("Dirtyboy.ttf", 50), base_color="#ffffff", hovering_color="#3399FF", size=(270, 60),)
            CONTINUE_BUTTON = Button(screen=self.__screen, pos=(500, 500 - 30),
                                     text_input="Continue", font=pygame.font.Font("Dirtyboy.ttf", 50), base_color="#ffffff", hovering_color="#3399FF", size=(220, 60),)
            GUIDE_BUTTON = Button(screen=self.__screen, pos=(80, 750 - 30),
                                  text_input="Guide", font=pygame.font.Font("Dirtyboy.ttf", 50), base_color="#ffffff", hovering_color="#3399FF", size=(150, 60),)
            QUIT_BUTTON = Button(screen=self.__screen, pos=(920, 750 - 30),
                                 text_input="Quit", font=pygame.font.Font("Dirtyboy.ttf", 50), base_color="#ffffff", hovering_color="#3399FF", size=(150, 60),)
            
            #set title game
            font = pygame.font.Font("./Dirtyboy.ttf", 100)
            text = font.render("Gomoku", True, "#ffffff")
            text_rect = text.get_rect(center=(500, 100))
            self.__screen.blit(text,text_rect)
            #set warning game event
            current_time = pygame.time.get_ticks()
            if self.error_data:
                self.draw_warning_continue()
            if current_time - self.time_press_btn > 1500:
                self.error_data = False
            # draw button
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            for button in [PVP_BUTTON, PVE_BUTTON, CONTINUE_BUTTON, GUIDE_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update()
            # check vent
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PVP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.init_btn()
                        self.pvp = True
                        self.running = False
                    if PVE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.init_btn()
                        self.pve = True
                        self.running = False
                    if CONTINUE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.init_btn()
                        self.time_press_btn = pygame.time.get_ticks()
                        self._continue = True
                        self.running = False
                    if GUIDE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.init_btn()
                        self.guide = True
                        self.running = False
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
            pygame.display.update()
            clock.tick(60)


class Button:
    def __init__(self, screen, pos, text_input, font, base_color, hovering_color, size, ):
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.x_size = size[0]
        self.y_size = size[1]
        self.font = font
        self.screen = screen
        self.base_color, self.hovering_color =  base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = pygame.draw.rect(self.screen,"#ffffff", ((
            self.x_pos-(self.x_size//2), self.y_pos-(self.y_size//2 -1)), (self.x_size, self.y_size)),1,20)
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    def update(self):
        self.screen.blit(self.text, self.text_rect)
    
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(
                self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(
                self.text_input, True, self.base_color)

        
