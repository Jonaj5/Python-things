hero_surface = pygame.image.load("Pygame/Space invaders/space_ship.png")
hero_rect = hero_surface.get_rect()
hero_rect.center = (1280//2, 640)

self.game.screen.blit(hero_surface, hero_rect)