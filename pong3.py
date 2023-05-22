import pygame

pygame.init()

WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('My Single Player Pong')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 255)

screen.fill(BLACK)
pygame.display.update()

radius = 25
x = WIDTH//2
y = HEIGHT//2
pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.


end = False
while not end:
    # fill screen with color only
  screen.fill(BLACK)
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
          end = True

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        # up left corner
      x -= radius
      y -=radius

    if key[pygame.K_d]:
        # up right corner
      x += radius
      y -=radius

    if key[pygame.K_s]:
        # down left corner
      x -= radius
      y +=radius
    if key[pygame.K_w]:
        # down left corner

      x += radius
      y +=radius


    # redraw circle at new position
      
    pygame.draw.circle(screen, WHITE, (x, y), radius)  # Position is the center of the circle.

    # update the display
    pygame.display.update()

pygame.quit()