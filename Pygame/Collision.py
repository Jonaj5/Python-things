import pygame, sys
from pygame. locals import *
from random import randrange

WIDTH, HEIGHT = 1280, 720

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

pygame.init()
clock = pygame.time.Clock()

Window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Collision")

rectangle1 = pygame.Rect(200,200,150,100)
rectangle2 = pygame.Rect(500,200,200,150)
rectangle3 = pygame.Rect(500,500,300,100)

gravity = 4

run = True

while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
        elif event.type== KEYUP and event.key == K_ESCAPE:
            run==False

        point = pygame.mouse.get_pos()
        collide1 = rectangle1.collidepoint(point)
        if collide1:
            color = RED
        else:
            color = WHITE
            
        rectangle2.top += gravity
        collide2 = rectangle3.colliderect(rectangle2)
        if collide2:
            rectangle3.bottom = rectangle2.top
        
        Window.fill(BLACK)
        pygame.draw.rect(Window, MAGENTA, rectangle2)
        pygame.draw.rect(Window, D_BLUE, rectangle3)
        pygame.draw.rect(Window, color, rectangle1)
        pygame.display.flip()
        
pygame.quit()
sys.exit()