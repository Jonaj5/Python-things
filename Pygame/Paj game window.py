import pygame, sys
from pygame. locals import *
from random import randrange

WIDTH, HEIGHT = 640, 480
X, Y=320, 240
RADIUS = 50

pygame.init()
clock = pygame.time.Clock()

Window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("First app")

BLACK   = pygame.Color("#000000")
D_BLUE    = pygame.Color("#0004dd")
BLUE    = pygame.Color("#005eff")
L_BLUE    = pygame.Color("#00e5ff")
CYAN    = pygame.Color("#22ff00")
GREEN   = pygame.Color("#22ff00")
YELLOW  = pygame.Color("#22ff00")
RED     = pygame.Color("#ff0000")
MAGENTA = pygame.Color("#dd00ff")
WHITE   = pygame.Color("#ffffff")

run = True

while run:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
        elif event.type== KEYUP and event.key == K_ESCAPE:
            run==False
    
    keys=pygame.key.get_pressed()
    if keys[K_LEFT] and X>RADIUS:
        X-=5
    if keys[K_RIGHT] and X<WIDTH-RADIUS:
        X+=5
    if keys[K_UP] and Y>RADIUS:
        Y-=5
    if keys[K_DOWN] and Y<HEIGHT-RADIUS:
        Y+=5
    
    clock.tick(120)
    Window.fill(BLACK)
    pygame.draw.circle(Window, GREEN, (X, Y), 50)
    pygame.display.flip()
    

pygame.quit()
sys.exit()