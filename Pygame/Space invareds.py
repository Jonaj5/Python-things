import pygame, sys
from pygame.locals import *
from random import randrange
1280, 720

class Game:
    screen = None
    alien = []
    rockets = []
    
    def __init__(self, width, height):
        pygame.init()
        self.height = height
        self.width = width
        self.screen = pygame.display.set_mode((width,height))
        self.clock = pygame.time.Clock()
        self.name = pygame.display.set_caption("Space invaders")
        run = True

        alien = Alien(self, 30, 30)
        hero = Hero(self, width/2, height-20)
        generator = Generator(self)
        
        while run:
            self.clock.tick(120)
            for event in pygame.event.get():
                if event.type == QUIT:
                    run=False
                elif event.type== KEYUP and event.key == K_ESCAPE:
                    run==False

                if event.type== KEYDOWN and event.key == K_SPACE:
                    self.rockets.append(Rocket(self, hero.x, hero.y))
                    
            pygame.display.flip()
            self.screen.fill("black")
            
            for alien in self.alien:  
                alien.draw()
            
            hero.draw()
              
            for rocket in self.rockets:
                rocket.draw()
  
            

class Alien:
    
    def __init__(self, game, x, y,):
        self.x = x
        self.y = y
        self.game = game
    
    def draw(self):
        pygame.draw.rect(self.game.screen,"orange", pygame.Rect(self.x, self.y, 30, 30))
        self.y += 0.08
 
        
class Hero:
    def __init__(self, game, x, y):
        self.x=x
        self.y=y
        self.game=game 
        
    def draw(self):
        game.screen.blit(pygame.image.load("Resources/space_ship.png"))


class Generator:
    def __init__(self, game):
        margin = 30
        gap = 50
        
        for x in range(margin, game.width-margin, gap):
            for y in range(margin, int(game.height/2), gap):
                game.alien.append(Alien(game, x, y))
            

class Rocket:

    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, 'salmon', pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2

       
game = Game(1280, 720)
