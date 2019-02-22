import pygame
from characters import Characters

class Hero(Characters):

    # Import Hero image
    hero_image = pygame.image.load("./images/hero.png")

    # Initialize with the location of the hero
    def __init__(self, x, y):
        Characters.__init__(self, x, y, 0, 0)
        self.image = pygame.image.load("./images/hero.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    def hero_dead(self):
        self.dead = True
        font = pygame.font.Font(None, 60)
        text = font.render("HA! You Lose!", True, (0, 0, 0))
        self.image = text
        self.x = 120
        self.y = 150
        self.dir_x = 0 
        self.dir_y = 0
            
    def hero_restart(self):
        self.image = pygame.image.load("./images/hero.png").convert_alpha()
        self.x = 256
        self.y = 240
        self.dir_x = 0
        self.dir_y = 0
        self.dead = False