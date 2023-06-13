import pygame
import random

colors = [
    (0, 0, 0),
    (120, 37, 179),
    (100, 179, 179),
    (80, 34, 22),
    (80, 134, 22),
    (180, 34, 22),
    (180, 34, 122),
]
class Figure:
    figures = [
        [[1, 5, 9, 13], [4, 5, 6, 7]],
        [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],
        [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  
        [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],
        [[1, 2, 5, 6]],
    ]
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.randint(0, len(self.figures)-1)
        self.color = random.randint(1, len(colors) -1)
        self.rotation = 0

    def image(self):
        return self.figures[self.type][self.rotation]
    
    def rotate(self):
        self.rotation = (self.rotation + 1) % len(self.figures[self.type])
  
class gameWindow:
    level, score, state, field, height, width, x, y, zoom, figure = 1, 0, "start", [], 0, 0, 100, 60, 20, None

    def __init__(self, height, width):
        self.height = height
        self.width = width
        for i in range(height):
            newLine = []
            for j in range(width):
                newLine.append(0)
            self.field.append(newLine)

    def newFigure(self):
        self.figure = Figure(3,0)
    def intersection(self):
        
        intersectionCheck = False
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    if i + self.figure.y > self.height - 1 or j + self.figure.x > self.width - 1 or j + self.figure.x < 0 or self.field[i + self.figure.y][j + self.figure.x] > 0:
                        intersectionCheck = True
        return intersectionCheck
    
    def lockInPlace(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.figure.image():
                    self.field[i + self.figure.y][j + self.figure.x] = self.figure.color
        self.breakLine()
        self.newFigure()
        if self.intersection():
            game.state = "gameover"
    
    def breakLine(self):
        lines = 0
        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros+=1
                if zeros == 0:
                    lines+=1
                    for n in range(i,1,-1):
                        for j in range(self.width):
                            self.field[n][j] = self.field[n - 1][j]
        self.score =+ lines ** 2

    def goSpace(self):
        while not self.intersection():
            self.figure.y += 1
        self.figure.y -= 1
        self.lockInPlace()
    
    def goDown(self):
        self.figure.y += 1
        if self.intersection():
            self.figure.y -= 1
            self.lockInPlace()
    
    def goS2S(self, direction):
        old = self.figure.x
        self.figure.x += direction
        if self.intersection():
            self.figure.x = old
    
    def rotate(self):
        old = self.figure.rotation
        self.figure.rotate()
        if self.intersection():
            self.figure.rotation = old

pygame.init()
BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)

size = (400,500)
screen = pygame.display.set_mode(size)

done = False
clock = pygame.time.Clock()
fps, counter = 25, 0
game = gameWindow(20,10)
downpress = False
while not done:
    if game.figure is None:
        game.newFigure()
    counter += 1
    if counter > 100000:
        coutner = 0
    if counter % (fps // game.level // 2 ) == 0 or downpress:
        if game.state == 'start':
            game.goDown()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                game.rotate()
            if event.key == pygame.K_DOWN:
                downpress = True
            if event.key == pygame.K_LEFT:
                game.goS2S(-1)
            if event.key == pygame.K_RIGHT:
                game.goS2S(1)
            if event.key == pygame.K_SPACE:
                game.goSpace()
            if event.key == pygame.K_ESCAPE:
                game.__init__(20, 10)
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_DOWN:
            downpress = False
    screen.fill(WHITE)
    for i in range(game.height):
        for j in range(game.width):
            pygame.draw.rect(screen, GRAY, [game.x + game.zoom * j, game.y + game.zoom * i, game.zoom, game.zoom], 1)
            if game.field[i][j] > 0:
                 pygame.draw.rect(screen, colors[game.field[i][j]], [game.x + game.zoom * j + 1, game.y + game.zoom * i + 1, game.zoom - 2, game.zoom - 1])
    if game.figure is not None:
        for i in range(4):
            for j in range(4):
                p = i * 4 + j
                if p in game.figure.image():
                    pygame.draw.rect(screen, colors[game.figure.color], [game.x + game.zoom * (j + game.figure.x) + 1, game.y + game.zoom * (i + game.figure.y) + 1, game.zoom - 2, game.zoom - 2])
    smallFont = pygame.font.SysFont('Comic sans', 25, True, False)
    bigFont = pygame.font.SysFont('Comic sans', 65, True, False)
    text = smallFont.render("Score = " + str(game.score), True, BLACK)
    gameoverText = bigFont.render("Game Over! Press ESC to close", True, (255,128,0))
    screen.blit(text, [0,0])
    if game.state == "gameover":
        screen.blit(gameoverText, [25,200])
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()  


            

