import pygame

class Characters(pygame.sprite.Sprite):
    
    # Initialize with x, y position as well as x,y speed
    def __init__(self, x, y, dir_x, dir_y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.dir_x = dir_x
        self.dir_y = dir_y
        self.dead = False
    
    # Function that controls the character's movement
    def character_movement(self):
        self.x += self.dir_x
        self.y += self.dir_y

    # Function that controls the character's boundaries
    def character_fence(self, option):
        # Hero Fence is Option 1
        if option == 1:
            if self.x + self.dir_x > 450:
                self.x = 450
            if self.x + self.dir_x < 33:
                self.x = 33
            if self.y + self.dir_y > 415:
                self.y = 415
            if self.y + self.dir_y < 33:
                self.y = 33
        # Monster Fence is Option 2
        if option == 2:
            if self.x + self.dir_x > 450: # If the Monster's next move is past the trees (RIGHT), go to the opposite direction
                self.x = 33
            if self.x + self.dir_x < 33: # If the Monster's next move is past the trees (LEFT), go to the opposite direction
                self.x = 450
            if self.y + self.dir_y > 415: # If the Monster's next move is past the trees (SOUTH), go to the opposite direction
                self.y = 33
            if self.y + self.dir_y < 33: # If the Monster's next move is past the trees (NORTH), go to the opposite direction
                self.y = 415

    def rect_update(self):
        self.rect.center = self.x, self.y