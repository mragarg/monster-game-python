import pygame

def main():
    width = 500
    height = 500
    background_iamge = pygame.image.load("background.png")

    #initialize pygame
    pygame.init()
    #set up the screen (drawing surface for the game)
    screen = pygame.display.set_mode((width, height))
    #setting a caption
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(background_iamge)

        # Game display

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
