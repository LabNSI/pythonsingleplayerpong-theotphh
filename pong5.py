import pygame
from random import randint, random

pygame.init()

WIDTH = 800
HEIGHT = 600
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

radius = 10
x = WIDTH / 2
y = radius*1.5

pygame.draw.circle(screen, WHITE, (x, y),
                   radius)  # Position is the center of the circle.

paddle = {"width": 200, 
          "height": 20, 
          "color": BLUE, 
          "x": WIDTH, 
          "y": HEIGHT}

paddle["x"] = WIDTH/2
paddle["y"] = HEIGHT - paddle["height"]*2
pygame.draw.rect(screen, paddle["color"],(paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

speed = 5
x_sens = y_sens = 1
pause = False

end = False
while not end:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

    key = pygame.key.get_pressed()

    if key[pygame.K_SPACE]:
        pause = True

    if key[pygame.K_RETURN]:
        pause = False

    if key[pygame.K_m]:
        auto = False

    if not pause:
        if key[pygame.K_LEFT] and paddle["x"] >= 0:
            print("Key LEFT pressed")
            paddle["x"] -= speed

        if key[pygame.K_RIGHT] and paddle["x"] + paddle["width"] <= WIDTH:
            print("Key RIGHT pressed")
            paddle["x"] += speed

        # change x direction if the ball hits the left or right edge
      
        if x <= 0+radius or x >= WIDTH-radius:
            x_sens = x_sens * -1
        # change y direction if the ball hits the top edge
        if y <= 0+radius :
            y_sens = y_sens * -1

        # if the ball hits the paddle top
       
    # if the ball is between the x paddle begin and the x paddle end
    #     ???
    # change y direction
    #        ???
        if y >= paddle["y"] - paddle["height"] / 2 and x >= paddle["x"] and x <= paddle["x"] + paddle["width"]:
            y_sens *= -1
    # if the ball comes out of the screen from below, end the game
    # ???
        if y >= HEIGHT-radius :
            end = True

    # compute the new ball coordinates
        x = x + x_sens * speed
        y = y + y_sens * speed

    # redraw ball and paddle
    pygame.draw.circle(screen, WHITE, (x, y), radius)
  #  print(x,y)
    pygame.draw.rect(screen, paddle["color"],(paddle["x"], paddle["y"], paddle["width"], paddle["height"]))

    # update screen
    pygame.display.update()
    pygame.time.delay(10)

pygame.quit()
