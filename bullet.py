import pygame
import math

from bullet_affiliation import BulletAffiliation
from camera_abc import CameraABC
from common import draw_text
from consts import BLACK
from ex_sprite import ExSprite
from position import Position


class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle: float, pos: Position, affiliation: BulletAffiliation, damage: float, bullet_speed: float, delta_speed: Position):

        self.__sprite = ExSprite('images/game/ship.png', color_key=BLACK, angle=angle)
        self.__pos = pos

        self.delta_pos = Position(bullet_speed * math.cos(angle), bullet_speed * math.sin(angle)) + delta_speed

        self.affiliation = affiliation
        self.damage = damage

        self.distance = 0
        self.__bullet_speed = bullet_speed

    def update(self):
        self.__pos += self.delta_pos
        self.distance += self.__bullet_speed

    def draw(self, sc: pygame.Surface, camera: CameraABC, is_debug: bool):

        screen_pos = camera.get_screen_pos(self.__pos)
        self.__sprite.draw(sc, screen_pos, is_debug)

        if is_debug:
            draw_text(sc, f'{self.__pos}', screen_pos + Position(0, -20))

    def get_rect(self) -> pygame.Rect:
        return self.__sprite.get_rotated_rect(self.__pos)
