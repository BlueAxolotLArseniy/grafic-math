import pygame
import math
import common
import consts

class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle: float, center: tuple):
        self.angle = angle
        
        self.x, self.y = center
        
        self.image = pygame.image.load('images/ship.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.original_image = self.image
        
        self.rect = self.image.get_rect(center=(self.x, self.y))
        
        self.delta_x = int(consts.BULLET_SPEED * math.cos(angle))
        self.delta_y = int(consts.BULLET_SPEED * math.sin(angle))

    def _rotate(self):
        self.image = pygame.transform.rotate(self.original_image, int(common.radians_to_degrees(-self.angle)))
        
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):
        self._rotate()

        self.rect.centerx += self.delta_x
        self.rect.centery += self.delta_y

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)
