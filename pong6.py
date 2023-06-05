import pygame
from random import randint, random

pygame.init()

Best_Score = 0

def Game(Best_Score) :
  
  WIDTH = 800
  HEIGHT = 600
  screen = pygame.display.set_mode((WIDTH, HEIGHT))
  Nb_de_5_score = 0
  Nb_de_10_score = 0
  pygame.display.set_caption('My Game')
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)
  RED = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLUE = (0, 0, 255)
  YELLOW = (255, 255, 255)
    
  myfont = pygame.font.SysFont('monospace', 35)
    
  print("pong6")
  screen.fill(BLACK)
  title = myfont.render("Single Player Pong:", False, GREEN)
  screen.blit(title, (WIDTH // 2 - title.get_width() // 2,
                        HEIGHT // 2 - title.get_height() * 2))
  pygame.display.update()
  pygame.time.delay(1000)
    
    # countdown before start game
    # loop from 3 to 0 and write the number in the middle of the screen
  for i in range(4):
      print(i)
    
      timer = myfont.render(str(3 - i), False, RED)
      pygame.draw.rect(screen, BLACK,
                        (WIDTH // 2 - timer.get_width() // 2,
                        HEIGHT // 2 - timer.get_height() * 1, 50,
                          50))  #cela enleve les précedent nombres de timer
    
      screen.blit(timer, (WIDTH // 2 - timer.get_width() // 2,
                            HEIGHT // 2 - timer.get_height() * 1))
      pygame.display.update()
    
      pygame.time.delay(1000)
    
  radius = 10
  x = WIDTH // 2
  y = radius * 1.5
  score = 0  
  pygame.draw.circle(screen, WHITE, (x, y),
                       radius)  # Position is the center of the circle.
    
  paddle = {"width": 200, "height": 20, "color": BLUE, "x": 0, "y": HEIGHT}
  paddle["x"] = WIDTH // 2 - paddle["width"] // 2
  paddle["y"] = HEIGHT - paddle["height"]
  pygame.draw.rect(screen, paddle["color"],
                   (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
    
  speed = 10
  x_sens = y_sens = 1
    
  pause = False
    
  end = False
  
  while not end:
      screen.fill(BLACK)
      ScoreDiplay = myfont.render("Score : " + str(score), False, GREEN)
      screen.blit(ScoreDiplay, (0, 0))

      ScoreDiplay = myfont.render("Best Score : " + str(Best_Score), False, GREEN)
      screen.blit(ScoreDiplay, (WIDTH - ScoreDiplay.get_width(),0))
      # Control the game
      # Past your code from pong5.py
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              end = True
  
          key = pygame.key.get_pressed()
  
          if key[pygame.K_SPACE]:
              pause = True
  
          if key[pygame.K_RETURN]:
              pause = False
  
      if not pause:
          if key[pygame.K_LEFT] and paddle["x"] >= 0:
              # print("Key LEFT pressed")
              paddle["x"] -= speed
  
          if key[pygame.K_RIGHT] and paddle["x"] + paddle["width"] <= WIDTH:
              #    print("Key RIGHT pressed")
              paddle["x"] += speed
  
          # change x direction if the ball hits the left or right edge
  
          if x <= 0 + radius or x >= WIDTH - radius:
              x_sens = x_sens * -1
          # change y direction if the ball hits the top edge
          if y <= 0 + radius:
              y_sens = y_sens * -1
  
          # if the ball hits the paddle top
  
      # if the ball is between the x paddle begin and the x paddle end
      #     ???
      # change y direction
      #        ???
          if y >= paddle["y"] - paddle["height"] / 2 and x >= paddle[
                  "x"] and x <= paddle["x"] + paddle["width"]:
              y_sens *= -1
  
              score += 1
              if Best_Score < score :
                Best_Score = score
                print(Best_Score,score)
              print(score // 5, Nb_de_5_score)
              if score // 10 > Nb_de_10_score:  # se fait a 11 ou 9
                  paddle["width"] -= 20
                  Nb_de_10_score += 1
              elif score // 5 > Nb_de_5_score:
                  speed += 2.5
                  Nb_de_5_score += 1
              
  
              pygame.display.update()
      # if the ball comes out of the screen from below, end the game
      # ???
          if y >= HEIGHT - radius:
              end = True
              myfont = pygame.font.SysFont('monospace', 35)
              RestartText = myfont.render(str("Press 'R' to restart "), False, WHITE)
              screen.blit(RestartText, (WIDTH // 2 - RestartText.get_width() // 2,
              HEIGHT // 2 - RestartText.get_height() * 1))
      # compute the new ball coordinates
          x = x + x_sens * speed
          y = y + y_sens * speed
  
      # redraw ball and paddle
      pygame.draw.circle(screen, WHITE, (x, y), radius)
      pygame.draw.rect(
          screen, paddle["color"],
          (paddle["x"], paddle["y"], paddle["width"], paddle["height"]))
  
      # Display the score in position (10, 0) (top left on the screen)
  
      pygame.display.update()
      pygame.time.delay(10)
  
  # Wait a bit to be sure the player knows his score
  pygame.time.delay(2000)
  return end,Best_Score
end,Best_Score = Game(Best_Score)
while end:
  
  for event in pygame.event.get():
      key = pygame.key.get_pressed()

      if key[pygame.K_r]:
        end,Best_Score = Game(Best_Score)

        