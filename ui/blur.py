from pygame import Surface
import pygame
from consts import SCREEN_HEIGHT, SCREEN_WIDTH


class Blur:

    def __init__(self):
        self.blur_sc = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, sc: Surface,):
        self.blur_sc.fill((0, 0, 0))
        self.blur_sc.set_alpha(180)
        sc.blit(self.blur_sc, (0, 0))
