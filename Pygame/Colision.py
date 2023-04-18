import pygame, sys
from pygame. locals import *
from random import randrange

WIDTH, HEIGHT = 640, 480

pygame.init()
clock = pygame.time.Clock()

Window = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Kolize")

run = True

while run:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
        elif event.type== KEYUP and event.key == K_ESCAPE:
            run==False
    

pygame.quit()
sys.exit()