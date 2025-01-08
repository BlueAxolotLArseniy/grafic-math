import pygame
from common import radians_to_degrees, get_angle_to_player
from player import Player


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, player: Player):
        self.image = pygame.image.load('images/enemy.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.player = player

    def _rotate(self):
        __angle = get_angle_to_player(self.rect.centerx, self.rect.centery,
                                      self.player.rect.centerx, self.player.rect.centery)
        self.image = pygame.transform.rotate(self.original_image, int(radians_to_degrees(-__angle)))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):
        self._rotate()

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)
