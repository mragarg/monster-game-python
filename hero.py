import pygame
from characters import Characters

class Hero(Characters):

    # Import Hero image
    hero_image = pygame.image.load("./images/hero.png")

    # Initialize with the location of the hero
    def __init__(self, x, y):
        Characters.__init__(self, x, y, 0, 0)
        self.image = pygame.image.load("./images/hero.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.dead = False
