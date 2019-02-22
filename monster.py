import random
import pygame
from characters import Characters

class Monster(Characters):

    # Import Monster image
    monster_image = pygame.image.load("./images/monster.png")
    
    # Initialize wih the starting speed and direction of the monster
    def __init__(self, x, y, dir_x, dir_y):
        Characters.__init__(self, x, y, dir_x, dir_y)
        self.change_mv_cd = 60
        self.image = pygame.image.load("./images/monster.png")
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.dead = False


    # Function countdowns the time until it has to randomize the movement. 
    # When countdown is 0, it will randomly change direction
    def monster_random_movement(self):
        self.change_mv_cd -= 1
        if self.change_mv_cd == 0:
            self.change_mv_cd = 60
            rand_direciton = random.randint(0,3)
            if rand_direciton == 0: # Go North
                self.dir_y = -self.dir_y
            if rand_direciton == 1: # Go Right
                self.dir_x = -self.dir_x
            if rand_direciton == 2: # Go South
                self.dir_y = -self.dir_y
            if rand_direciton == 3: # Go Left
                self.dir_x = -self.dir_x

    # Function that updates the monster's attributes after collision
    def is_dead(self):
        self.dead = True
        font = pygame.font.Font(None, 60)
        text = font.render("You Win!", True, (0, 0, 0))
        self.image = text
        self.x = 172
        self.y = 150
        self.dir_x = 0 
        self.dir_y = 0

    def monster_restart(self):
        self.image = pygame.image.load("./images/monster.png")
        self.x = random.randint(40, 440)
        self.y = random.randint(40, 400)
        self.dir_x = 3
        self.dir_y = 3
        self.dead = False