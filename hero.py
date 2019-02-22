import pygame

class Hero(pygame.sprite.Sprite):

    # Import Hero image
    hero_image = pygame.image.load("./images/hero.png")

    # Initialize with the location of the hero
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dir_x = 0
        self.dir_y = 0
        self.image = pygame.image.load("./images/hero.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

    # Function involved in moving the Hero character around
    def hero_move(self):
        self.x += self.dir_x
        self.y += self.dir_y

    # Function involved in keeping the hero within the fence
    def hero_fence(self):
        if self.x + self.dir_x > 450:
            self.x = 450
        if self.x + self.dir_x < 33:
            self.x = 33
        if self.y + self.dir_y > 415:
            self.y = 415
        if self.y + self.dir_y < 33:
            self.y = 33

    # Function updates the rect.center of the current position (collision)
    def rect_update(self):
        self.rect.center = self.x, self.y

