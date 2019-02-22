import pygame
import time
import random
from monster import Monster
from hero import Hero
from characters import Characters

# Key Stroke Variables
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def main():
    # Initialize pygame
    pygame.init()

    # Importing image
    background_image = pygame.image.load("./images/background.png")
    
    # Importing and Intialize Sound
    pygame.mixer.init()
    bg_sound = pygame.mixer.Sound("./sounds/music.wav")
    lose_sound = pygame.mixer.Sound("./sounds/lose.wav")
    win_sound = pygame.mixer.Sound("./sounds/win.wav")

    # Window size
    window_width = 512
    window_height = 480

    # Set up the screen (drawing surface for the game)
    screen = pygame.display.set_mode((window_width, window_height))
    
    # Game Window Title
    pygame.display.set_caption('Monster Game')
    
    # Calls the Clock object and sets it to variable clock (for shorthand purposes)
    clock = pygame.time.Clock()


    ########## Game initialization ##########

    # Created a monster instance
    game_monster = Monster(120, 120, 1, 1)
    game_hero = Hero(256, 240)

    # Sprite Groups
    monster_group = pygame.sprite.Group()
    monster_group.add(game_monster)

    hero_group = pygame.sprite.Group()
    hero_group.add(game_hero)

    # FPS settings
    FPS = 60

    ########## While loop used to have the game continuously run ##########
    stop_game = False
    while not stop_game:

        # Event is for user input such as keypress to clicks
        for event in pygame.event.get():

            # Hero Key Strokes Movement
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
        screen.blit(game_hero.image, [game_hero.x, game_hero.y])
        screen.blit(game_monster.image, [game_monster.x, game_monster.y])

        # Hero Movement
        game_hero.character_movement()
        game_hero.character_fence(1)
        game_hero.rect_update()

        # Monster Movement
        game_monster.monster_random_movement()
        game_monster.character_movement()        
        game_monster.character_fence(2)
        game_monster.rect_update()

        # Sprite Collide
        collide = pygame.sprite.spritecollide(game_hero, monster_group, True)

        if collide:
            game_hero.x = 230
            game_hero.y = 200
            game_monster.is_dead()
            win_sound.play()


        # Game display
        pygame.display.update()

        # Set the tick rate to 60 ms, which means the game runs at 60 FPS
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
