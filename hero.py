import pygame

class Hero():

    # Import Hero image
    hero_image = pygame.image.load("./images/hero.png")

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dir_x = 0
        self.dir_y = 0

    def hero_move(self):
        self.x += self.dir_x
        self.y += self.dir_y

    def hero_fence(self):
        if self.x + self.dir_x > 450:
            self.x = 450
        if self.x + self.dir_x < 33:
            self.x = 33
        if self.y + self.dir_y > 415:
            self.y = 415
        if self.y + self.dir_y < 33:
            self.y = 33