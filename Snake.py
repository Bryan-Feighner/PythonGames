import pygame
import time
import random

speed = 17
windowx=1920
windowy=1080
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
score = 0
snPos = [100, 50]
snBod = [[500,200],[490,200],[480,200],[470,200]]
frPos = [random.randrange(1, (windowx/10))*10, random.randrange(1,(windowy/10))*10]
frSpawn = True
direction = 'RIGHT'
change = direction
fps = pygame.time.Clock()
gameWindow = pygame.display.set_mode((windowx,windowy))
pygame.display.set_caption('Bryans first foray into Python Game Coding!')
pygame.init()
def showScore(choice, color, font, size):
    scoreFont = pygame.font.SysFont(font, size)
    scoreSurface = scoreFont.render('Score = ' + str(score), True, color)
    scoreRect = scoreSurface.get_rect()
    gameWindow.blit(scoreSurface, scoreRect)
def gameOver():
    goFont = pygame.font.SysFont('comic sans', 50)
    goSurface = goFont.render('Your final score is ' + str(score), True, red)
    goRect = goSurface.get_rect()
    goRect.midtop = (windowx/2,windowy/4)
    gameWindow.blit(goSurface, goRect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()
while True:
   
    # handling key events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                change = 'UP'
            if event.key == pygame.K_DOWN:
                change = 'DOWN'
            if event.key == pygame.K_LEFT:
                change = 'LEFT'
            if event.key == pygame.K_RIGHT:
                change = 'RIGHT'
    if change == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'
    if direction == 'UP':
        snPos[1] -= 10
    if direction == 'DOWN':
        snPos[1] += 10
    if direction == 'LEFT':
        snPos[0] -= 10
    if direction == 'RIGHT':
        snPos[0] += 10
    snBod.insert(0, list(snPos))
   
    if snPos[0] == frPos[0] and snPos[1] == frPos[1]:
        score += 10
        frSpawn = False
    else:
        snBod.pop()
    if not frSpawn:
        frPos = [random.randrange(1, (windowx//10)) * 10,
                          random.randrange(1, (windowy//10)) * 10]
    frSpawn = True
    gameWindow.fill(black)
    for pos in snBod:
        pygame.draw.rect(gameWindow, green, pygame.Rect(
          pos[0], pos[1], 10, 10))
         
    pygame.draw.rect(gameWindow, white, pygame.Rect(
      frPos[0], frPos[1], 10, 10))
    if snPos[0] < 0 or snPos[0] > windowx-10:
        gameOver()
    if snPos[1] < 0 or snPos[1] > windowy-10:
        gameOver()
    for block in snBod[1:]:
        if snPos[0] == block[0] and snPos[1] == block[1]:
            gameOver()
    showScore(1, white, 'times new roman', 20)
    pygame.display.update()
    fps.tick(speed)





