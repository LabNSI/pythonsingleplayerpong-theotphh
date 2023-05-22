import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Single Player Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

SCREEN.fill(BLACK)
pygame.display.update()

end = False
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

pygame.quit()