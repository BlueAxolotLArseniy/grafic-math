
import pygame
from pygame import Surface
from math import cos, sin


class Bullet(pygame.sprite.Sprite):

    def __init__(self, angle: float, speed: float, x: int, y: int):
        # self.__angle = angle
        # self.__speed = speed
        self.image = pygame.image.load('images/ship.png').convert()
        self.rect = self.image.get_rect(center=(x, y))
        self.delta_x = int(speed * cos(angle))
        self.delta_y = int(speed * sin(angle))

    def update(self):
        self.rect.centerx += self.delta_x
        self.rect.centery += self.delta_y

    def draw(self, sc: Surface):
        sc.blit(self.image, self.rect)
