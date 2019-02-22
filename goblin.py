import random
import pygame
from monster import Monster

class Goblin(Monster):

    goblin_image = pygame.image.load("./images/goblin.png")

    def __init__(self, x, y):
        Monster.__init__(self, x, y, 1, 1)
        self.image = pygame.image.load("./images/goblin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y 

    def goblin_restart(self):
        self.image = pygame.image.load("./images/goblin.png").convert_alpha()
        self.x = random.randint(40, 440)
        self.y = random.randint(40, 400)
        self.dir_x = 1
        self.dir_y = 1
        self.dead = False
