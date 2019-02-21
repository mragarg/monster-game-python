import random
import pygame

class Monster():

    # Import Monster image
    monster_image = pygame.image.load("./images/monster.png")
    
    def __init__(self, x, y, dir_x, dir_y):
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y 
        self.change_mv_cd = 60

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

    # Function 'controls' the monsters movement. It creates a fence in where it can stay
    def monster_fence(self):
        if self.x + self.dir_x > 459: # If the Monster's next move is past the trees (RIGHT), go to the opposite direction
            self.x = 33
        if self.x + self.dir_x < 33: # If the Monster's next move is past the trees (LEFT), go to the opposite direction
            self.x = 459
        if self.y + self.dir_y > 422: # If the Monster's next move is past the trees (SOUTH), go to the opposite direction
            self.y = 33
        if self.y + self.dir_y < 33: # If the Monster's next move is past the trees (NORTH), go to the opposite direction
            self.y = 422

    # Function that is responsible for the monster's continuous movement
    def monster_move(self):
        self.x += self.dir_x
        self.y += self.dir_y