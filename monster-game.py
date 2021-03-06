import pygame
import time
import random
from monster import Monster
from hero import Hero
from characters import Characters
from goblin import Goblin

# Key Stroke Variables
KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_ENTER = 13

# Other Variables
level_count = 1
bg_sound_path = "./sounds/music.wav"
lose_sound_path = "./sounds/lose.wav"
win_sound_path = "./sounds/win.wav"
bg_image_path = "./images/background.png"
window_width = 512
window_height = 480

def restart_level(monster, hero, goblin1, goblin2, goblin3):
    monster.monster_restart()
    hero.hero_restart()
    goblin1.goblin_restart()
    goblin2.goblin_restart()
    goblin3.goblin_restart()

def main():

    # Initialize pygame
    pygame.init()

    # Importing image
    background_image = pygame.image.load(bg_image_path)
    
    # Importing and Intialize Sound
    pygame.mixer.init()
    bg_sound = pygame.mixer.Sound(bg_sound_path)
    lose_sound = pygame.mixer.Sound(lose_sound_path)
    win_sound = pygame.mixer.Sound(win_sound_path)

    # Set up the screen (drawing surface for the game)
    screen = pygame.display.set_mode((window_width, window_height))
    
    # Game Window Title
    pygame.display.set_caption('Monster Game')
    
    # Calls the Clock object and sets it to variable clock (for shorthand purposes)
    clock = pygame.time.Clock()


    #################### Game initialization ####################

    # Created a monster instance
    game_monster = Monster(120, 120, 3, 3)
    game_hero = Hero(256, 240)
    game_goblin1 = Goblin(360, 360)
    game_goblin2 = Goblin(360, 360)
    game_goblin3 = Goblin(360, 360)

    # Sprite Groups
    monster_group = pygame.sprite.Group()
    monster_group.add(game_monster)

    hero_group = pygame.sprite.Group()
    hero_group.add(game_hero)

    goblin_group = pygame.sprite.Group()
    goblin_group.add(game_goblin1)
    goblin_group.add(game_goblin2)
    goblin_group.add(game_goblin3)

    # FPS settings
    FPS = 60

    # Music Start
    bg_sound.play()

    #################### While loop used to have the game continuously run ####################
    stop_game = False
    while not stop_game:

        # Event is for user input such as keypress to clicks
        for event in pygame.event.get():

            #Key Strokes Movement (Hero Movement and Enter Key)
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    if game_hero.dead == False:
                        game_hero.dir_y = 3
                elif event.key == KEY_UP:
                    if game_hero.dead == False:
                        game_hero.dir_y = -3
                elif event.key == KEY_LEFT:
                    if game_hero.dead == False:
                        game_hero.dir_x = -3
                elif event.key == KEY_RIGHT:
                    if game_hero.dead == False:
                        game_hero.dir_x = 3
                elif event.key == KEY_ENTER:
                    print("Enter Works")
                    restart_level(game_monster, game_hero, game_goblin1, game_goblin2, game_goblin3)
                    monster_group.add(game_monster)
                    goblin_group.add(game_goblin1)
                    goblin_group.add(game_goblin2)
                    goblin_group.add(game_goblin3)
                    bg_sound.play()
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
        screen.blit(game_goblin1.image, [game_goblin1.x, game_goblin1.y])
        screen.blit(game_goblin2.image, [game_goblin2.x, game_goblin2.y])
        screen.blit(game_goblin3.image, [game_goblin3.x, game_goblin3.y])

        # Hero Movement
        game_hero.character_movement()
        game_hero.character_fence(1)
        game_hero.rect_update()

        # Monster Movement
        game_monster.monster_random_movement()
        game_monster.character_movement()        
        game_monster.character_fence(2)
        game_monster.rect_update()

        # Goblin Movement
        game_goblin1.monster_random_movement()
        game_goblin1.character_movement()
        game_goblin1.character_fence(2)
        game_goblin1.rect_update()
        game_goblin2.monster_random_movement()
        game_goblin2.character_movement()
        game_goblin2.character_fence(2)
        game_goblin2.rect_update()
        game_goblin3.monster_random_movement()
        game_goblin3.character_movement()
        game_goblin3.character_fence(2)
        game_goblin3.rect_update()

        # Sprite Collide
        collide_monster = pygame.sprite.spritecollide(game_hero, monster_group, True)
        collide_goblin = pygame.sprite.spritecollide(game_hero, goblin_group, True)

        if collide_monster:
            bg_sound.stop()
            game_hero.x = 230
            game_hero.y = 200
            game_monster.is_dead()
            win_sound.play()

        if collide_goblin:
            bg_sound.stop()
            game_monster.x = 500
            game_monster.y = 500
            game_hero.hero_dead()
            lose_sound.play()
            game_monster.dir_x = 0
            game_monster.dir_y = 0

        if game_monster.dead == True:
            font = pygame.font.Font(None, 20)
            play_again_text = font.render("Press `Enter` to Play Again!", True, (0, 0, 0))
            screen.blit(play_again_text, [172, 220])
            game_hero.x = 236
            game_hero.y = 185

        if game_hero.dead == True:
            font = pygame.font.Font(None, 20)
            play_again_text = font.render("Press `Enter` to Play Again!", True, (0, 0, 0))
            screen.blit(play_again_text, [172, 220])
            game_goblin1.x = 236
            game_goblin1.y = 185
            game_goblin2.x = 236
            game_goblin2.y = 185
            game_goblin3.x = 236
            game_goblin3.y = 185
            game_hero.dir_x = 0 
            game_hero.dir_y = 0

        # Game display
        pygame.display.update()

        # Set the tick rate to 60 ms, which means the game runs at 60 FPS
        clock.tick(FPS)

    pygame.quit()

if __name__ == '__main__':
    main()
