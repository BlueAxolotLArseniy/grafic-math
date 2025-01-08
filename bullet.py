import pygame
from math import cos, sin
from common import radians_to_degrees


class Bullet(pygame.sprite.Sprite):

    def __init__(self, angle: float, speed: float, x: int, y: int):
        self.__angle = angle
        # self.__speed = speed
        self.image = pygame.image.load('images/ship.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.delta_x = int(speed * cos(angle))
        self.delta_y = int(speed * sin(angle))

    def _rotate(self):
        self.image = pygame.transform.rotate(self.original_image, int(radians_to_degrees(-self.__angle)))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):

        self._rotate()

        self.rect.centerx += self.delta_x
        self.rect.centery += self.delta_y

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)
