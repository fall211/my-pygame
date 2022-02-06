import pygame
from sys import exit
from settings import *
from level import GameLevel, MenuLevel
from map import PlayButton

class Game:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('My Game')
        self.clock = pygame.time.Clock()

        self.gamelevel = GameLevel()
        self.menulevel = MenuLevel()

    def MainGame(self):
        while True: #everything happens in this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.gamelevel.run()

            pygame.display.update() #update the screen when While True is on
            self.clock.tick(fps)

    def MainMenu(self):
        while True: #everything happens in this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.menulevel.run()


            if PlayButton().start_game() == True:
                Game().MainGame()

            pygame.display.update() #update the screen when While True is on
            self.clock.tick(fps)

    def Options(self):
        while True: #everything happens in this loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()



            pygame.display.update() #update the screen when While True is on
            self.clock.tick(fps)


if __name__ == '__main__':
	Game().MainMenu()
