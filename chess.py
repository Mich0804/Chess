# Example file showing a basic pygame "game loop"
import pygame

height = 720
width = 720
square_size = width/8

# pygame setup
pygame.init()
screen = pygame.display.set_mode((height, width))
clock = pygame.time.Clock()
running = True

white = (255, 255, 255)
black = (0, 0, 0)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(white)

    # RENDER YOUR GAME HERE

    knight = pygame.image.load("white pawn.png").convert()
    
    for x in range(1, 9, 2):
        for y in range(0, 8, 2):
            pygame.draw.rect(screen, black, (x * square_size, y * square_size, square_size, square_size))

    for x in range(0, 8, 2):
        for y in range(1, 9, 2):
            pygame.draw.rect(screen, black, (x * square_size, y * square_size, square_size, square_size))

    for x in range(0, 8):
        for y in range(0, 8):
            screen.blit(knight, (x * square_size + 20, y * square_size + 20))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

    chessboard = [['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
                  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                  ['0', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '0'],
                  ['0', '0', '0', '0', '0', '0', '0', '0'],
                  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]

pygame.quit()
