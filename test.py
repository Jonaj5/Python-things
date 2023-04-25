import pygame 
from pygame.locals import *


class Game:

    screen = None
    aliens = []

    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        finished = False

        generator = Generator(self)
        hero = Hero(self, width/2, height-20)


        while not finished:
            for event in pygame.event.get():
                if event.type == QUIT:
                    finished = True

            pygame.display.flip()
            self.clock.tick(60)
            self.screen.fill('skyblue')

            for alien in self.aliens:
                alien.draw()
            hero.draw()



class Alien:

    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, 'orange', pygame.Rect(self.x, self.y, 30, 30))
        self.y += 0.08


class Hero:
    
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game

    def draw(self):
        pygame.draw.rect(self.game.screen, 'red3', pygame.Rect(self.x, self.y, 16, 8))


class Generator:

    def __init__(self, game):
        margin = 30
        gap = 50

        for x in range(margin, game.width-margin, gap):
            for y in range(margin, int(game.height/2), gap):
                game.aliens.append(Alien(game, x, y))



game = Game(600, 400)
