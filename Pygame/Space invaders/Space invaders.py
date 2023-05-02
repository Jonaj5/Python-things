import pygame 
from pygame.locals import *

hero_surface = pygame.image.load("space_ship.png")
hero_rect = hero_surface.get_rect()

alien_surface = pygame.image.load("Pygame/Space invaders/space_invader.png")
alien_rect = alien_surface.get_rect()

class Game:

    screen = None
    aliens = []
    rockets = []
    

    def __init__(self, width, height):
        
        pygame.init()
        pygame.display.set_caption("Space invaders")
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        finished = False

        generator = Generator(self)
        hero = Hero(self, width/2, height-60)
        


        while not finished:
            
            keys = pygame.key.get_pressed()
            
            if keys[K_a]:
                hero.x -= 2 if hero.x > 40 else 0
            elif keys[K_d]:
                hero.x += 2 if hero.x < width-40 else 0
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    finished = True

                if event.type == KEYDOWN and event.key == K_SPACE:
                    self.rockets.append(Rocket(self, hero.x, hero.y))
                    

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill('black')

            for alien in self.aliens:
                alien.draw()
                alien.checkCollision(self)  

            hero.draw()
            
            for rocket in self.rockets:
                rocket.draw()



class Alien:
    
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.size = 40    

    def draw(self):
        alien_rect.center = (self.x, self.y)
        self.game.screen.blit(alien_surface, alien_rect)
        self.y += 0.08
            
    def checkCollision(self, game): 
        for rocket in game.rockets:
            if (rocket.x < self.x + self.size and
                rocket.x > self.x - self.size and
                rocket.y < self.y + self.size and
                rocket.y > self.y - self.size):

                game.rockets.remove(rocket)
                game.aliens.remove(self)


class Hero:
    
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        hero_rect.center = (self.x, self.y)
        self.game.screen.blit(hero_surface, hero_rect)


class Generator:

    def __init__(self, game):
        margin = 30
        gap = 50

        for x in range(margin, game.width-margin, gap):
            for y in range(margin, int(game.height/2), gap):
                game.aliens.append(Alien(game, x, y))


class Rocket:

    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, 'red', pygame.Rect(self.x, self.y, 2, 4))
        self.y -= 2



game = Game(1280, 720)

