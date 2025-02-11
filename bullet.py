import pygame
import math

from bullet_affiliation import BulletAffiliation
from common import rotate_image
from consts import BLACK, BULLET_SPEED, GREEN
from state import GameState


class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle: float, center: tuple, affiliation: BulletAffiliation, koefficient: float, game_state: GameState):
        self.angle = angle

        self.image = pygame.image.load('images/game_textures/ship.png').convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (self.image.get_width(), self.image.get_height()))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=center)

        self.delta_x = int(BULLET_SPEED * math.cos(angle))
        self.delta_y = int(BULLET_SPEED * math.sin(angle))

        self.affiliation = affiliation
        self.koefficient = koefficient

        self.game_state = game_state

    def update(self, kx, ky):
        self.image, self.rect = rotate_image(self.original_image, self.rect.center, self.angle)

        self.rect.centerx += self.delta_x
        self.rect.centery += self.delta_y

        self.rect.x += kx
        self.rect.y += ky

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, GREEN, self.rect, 2)
