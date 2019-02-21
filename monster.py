import pygame

def main():
    # Initialize pygame
    pygame.init()

    # Importing images
    background_iamge = pygame.image.load("./images/background.png")
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

    # Game initialization

    stop_game = False
    while not stop_game:

        # Event is for user input such as keypress to clicks
        for event in pygame.event.get():

            # Event that if user clicks exit
            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Uses the uploaded background image as the game background
        screen.blit(background_iamge, [0, 0])
        # Uses the uploaded hero image and places it in the middle of the screen
        screen.blit(hero_image, [256, 240])

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
