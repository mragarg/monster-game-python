import pygame
import time
import random
from monster import Monster

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
    hero_image = pygame.image.load("./images/hero.png")

    # Window size
    window_width = 512
    window_height = 480

    # Set up the screen (drawing surface for the game)
    screen = pygame.display.set_mode((window_width, window_height))
    
    # Game Window Title
    pygame.display.set_caption('Monster Game')
    
    # Calls the Clock object and sets it to variable clock (for shorthand purposes)
    clock = pygame.time.Clock()

    ################################    HERO    ################################
    hero_x = 256
    hero_y = 240
    hero_dir_x = 0
    hero_dir_y = 0



    # Game initialization

    # Created a monster instance
    game_monster = Monster(120, 120, 3, 3)

    # While loop used to have the game continuously run
    stop_game = False
    while not stop_game:

        # Event is for user input such as keypress to clicks
        for event in pygame.event.get():

            ################################ HERO MOVEMENT ################################
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero_dir_y = 3
                elif event.key == KEY_UP:
                    hero_dir_y = -3
                elif event.key == KEY_LEFT:
                    hero_dir_x = -3
                elif event.key == KEY_RIGHT:
                    hero_dir_x = 3
            if event.type == pygame.KEYUP:
                if event.key == KEY_DOWN:
                    hero_dir_y = 0
                elif event.key == KEY_UP:
                    hero_dir_y = 0
                elif event.key == KEY_LEFT:
                    hero_dir_x = 0
                elif event.key == KEY_RIGHT:
                    hero_dir_x = 0

            # Event that if user clicks exit
            if event.type == pygame.QUIT:
                stop_game = True

        # Game logic

        # Renders background, monster, and hero image
        screen.blit(background_image, [0, 0])
        screen.blit(hero_image, [hero_x, hero_y])
        screen.blit(game_monster.monster_image, [game_monster.x, game_monster.y])

        # Game display
        pygame.display.update()
        
        ################################ HERO MOVEMENT ################################
        hero_x += hero_dir_x
        hero_y += hero_dir_y

        # Monster Movement
        game_monster.monster_random_movement()
        game_monster.monster_move()        
        game_monster.monster_fence()

        # Set the tick rate to 60 ms, which means the game runs at 60 FPS
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
