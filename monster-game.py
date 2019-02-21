import pygame
import time
import random
from monster import Monster
from hero import Hero

# Key Stroke Variables
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def main():
    # Initialize pygame
    pygame.init()

    # Importing images
    background_image = pygame.image.load("./images/background.png")

    # Window size
    window_width = 512
    window_height = 480

    # Set up the screen (drawing surface for the game)
    screen = pygame.display.set_mode((window_width, window_height))
    
    # Game Window Title
    pygame.display.set_caption('Monster Game')
    
    # Calls the Clock object and sets it to variable clock (for shorthand purposes)
    clock = pygame.time.Clock()


    # Game initialization

    # Created a monster instance
    game_monster = Monster(120, 120, 3, 3)
    game_hero = Hero(256, 240)
    # While loop used to have the game continuously run
    stop_game = False
    while not stop_game:

        # Event is for user input such as keypress to clicks
        for event in pygame.event.get():

            ################################ HERO MOVEMENT ################################
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    game_hero.dir_y = 3
                elif event.key == KEY_UP:
                    game_hero.dir_y = -3
                elif event.key == KEY_LEFT:
                    game_hero.dir_x = -3
                elif event.key == KEY_RIGHT:
                    game_hero.dir_x = 3
            if event.type == pygame.KEYUP:
                if event.key == KEY_DOWN:
                    game_hero.dir_y = 0
                elif event.key == KEY_UP:
                    game_hero.dir_y = 0
                elif event.key == KEY_LEFT:
                    game_hero.dir_x = 0
                elif event.key == KEY_RIGHT:
                    game_hero.dir_x = 0

            # Event that if user clicks exit
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Renders background, monster, and hero image
        screen.blit(background_image, [0, 0])
        screen.blit(game_hero.hero_image, [game_hero.x, game_hero.y])
        screen.blit(game_monster.monster_image, [game_monster.x, game_monster.y])

        # Hero Movement
        game_hero.hero_move()
        game_hero.hero_fence()

        # Monster Movement
        game_monster.monster_random_movement()
        game_monster.monster_move()        
        game_monster.monster_fence()
        
        # Game display
        pygame.display.update()
        


        # Set the tick rate to 60 ms, which means the game runs at 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
