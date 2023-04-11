import pygame
from random import randint, choice

WIDTH = 800
HEIGHT = 600

BLACK = pygame.Color("#000000")
D_BLUE = pygame.Color("#0004dd")
BLUE = pygame.Color("#005eff")
L_BLUE = pygame.Color("#00e5ff")
CYAN = pygame.Color("#22ffff")
GREEN = pygame.Color("#22ff22")
YELLOW = pygame.Color("#ffff22")
RED = pygame.Color("#ff0000")
MAGENTA = pygame.Color("#dd00ff")
WHITE = pygame.Color("#ffffff")

polomer = 25
colors = [GREEN, BLUE, RED, WHITE, D_BLUE, L_BLUE, CYAN, YELLOW, MAGENTA]

class Ball:
    def __init__(self):
        self.x = randint(polomer, WIDTH - polomer)
        self.y = randint(polomer, HEIGHT - polomer)
        self.dx = randint(-5, 5)
        self.dy = randint(-5, 5)
        self.color = choice(colors)
        
    def move(self):
        self.x += self.dx
        self.y += self.dy
        
        if not polomer < self.x < WIDTH - polomer:
            self.dx = -self.dx
            self.color = choice(colors)
            
        if not polomer < self.y < HEIGHT - polomer:
            self.dy = -self.dy
            self.color = choice(colors)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Odraz")
clock = pygame.time.Clock()

balls = [Ball(), Ball(), Ball()]

running = True
while running:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    for ball in balls:
        ball.move()
        
    screen.fill(BLACK)
    for ball in balls:
        pygame.draw.circle(screen, ball.color, (ball.x, ball.y), polomer)

    pygame.display.flip()

pygame.quit()