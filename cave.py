import pygame

class Cave(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/game_textures/cave.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*15, self.image.get_height()*15))
        
        self.rect = self.image.get_rect(center=(x, y))
        
    def update(self, kx, ky):
        self.rect.x += kx
        self.rect.y += ky

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)
