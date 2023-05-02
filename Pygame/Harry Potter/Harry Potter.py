import pygame, sys
from pygame. locals import *
from random import randrange

WIDTH, HEIGHT = 1280, 720

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Harry Potter")

player_init_lives = 5
player_current_lives = player_init_lives
player_speed = 5

egg_init_speed = 5
egg_current_speed = egg_init_speed
egg_acceleration = 0.5
egg_hidden_cord = 100

score = 0

game_font_big = pygame.font.Font("Pygame/Harry Potter/harry.ttf", 50)
game_font_small = pygame.font.Font("Pygame/Harry Potter/harry.ttf", 30)

game_surface = game_font_big.render("Harry Potter a Ohnivy pohar", True, "gold3")
game_rect = game_surface.get_rect()
game_rect.center = (WIDTH//2, 30)

endgame_surface = game_font_big.render("Game Over", True, "gold3")
endgame_rect = endgame_surface.get_rect()
endgame_rect.center = (WIDTH//2, HEIGHT//2)

newgame_surface = game_font_small.render("Chces novou hru?", True, "gold3")
newgame_rect = newgame_surface.get_rect()
newgame_rect.center = (WIDTH//2, HEIGHT//2+60)

harry_surface = pygame.image.load("Pygame/Harry Potter/harry.png")
harry_rect = harry_surface.get_rect()
harry_rect.center = (100, HEIGHT//2)

egg_surface = pygame.image.load("Pygame/Harry Potter/egg.png")
egg_rect = egg_surface.get_rect()
egg_rect.x = WIDTH + egg_hidden_cord
egg_rect.y = randrange(60, HEIGHT-50)

hriste_suface = pygame.image.load("Pygame/Harry Potter/hriste.png")
hriste_rect = hriste_suface.get_rect()
hriste_rect.center = (WIDTH//2, (HEIGHT+60)//2)

run = True

while run:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            run=False
        elif event.type == KEYUP and event.key == K_ESCAPE:
            run=False
            
    keys = pygame.key.get_pressed()
    
    if keys[K_w] and harry_rect.top > 60:
        harry_rect.y -= player_speed
        
    elif keys[K_s] and harry_rect.bottom < HEIGHT:
        harry_rect.y += player_speed
    
    if egg_rect.x < 0:
        player_current_lives -= 1
        egg_rect.x = WIDTH + egg_hidden_cord
        egg_rect.y = randrange(60, HEIGHT-50)
    
    else:
        egg_rect.x -= egg_current_speed
        
    lives_surface = game_font_small.render(f"Zivoty: {player_current_lives}", True, "gold3")
    lives_rect = lives_surface.get_rect()
    lives_rect.right = WIDTH-20
    lives_rect.top = 15
    
    if harry_rect.colliderect(egg_rect):
        score += 1
        egg_current_speed += egg_acceleration
        egg_rect.x = WIDTH + egg_hidden_cord
        egg_rect.y = randrange(60, HEIGHT - 50)
    
    score_surface = game_font_small.render(f"Score: {score}", True, "gold3")
    score_rect = game_surface.get_rect()
    score_rect.left = 20
    score_rect.top = 15
    
    screen.fill("black")
    screen.blit(hriste_suface, hriste_rect)
    screen.blit(game_surface, game_rect)
    screen.blit(score_surface, score_rect)
    screen.blit(lives_surface, lives_rect)
    screen.blit(harry_surface, harry_rect)
    screen.blit(egg_surface, egg_rect)
    pygame.draw.line(screen, "gold3", (0, 60), (WIDTH, 60), 2)
    
    if player_current_lives == 0:
        screen.blit(endgame_surface, endgame_rect)
        screen.blit(newgame_surface, newgame_rect)
        pygame.display.update()
        
        pause = True
        while pause:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    score = 0
                    player_current_lives = player_init_lives
                    egg_current_speed = egg_init_speed
                    harry_rect.y = HEIGHT//2
                    pause = False
                    
                elif event.type == QUIT:
                    pause == False
                    run == False
    
    pygame.display.update()
    clock.tick(120)
    
pygame.quit()
sys.exit()