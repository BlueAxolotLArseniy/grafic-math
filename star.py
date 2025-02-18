
import pygame
from camera_abc import CameraABC
from color import Color
from consts import GAME_FIELD_RECT
from position import Position
from random import random


class Star:

    MAX_RADIUS = 4

    @classmethod
    def random(cls) -> 'Star':
        radius = random()*Star.MAX_RADIUS
        return Star(
            pos=Position.random(GAME_FIELD_RECT) * (Star.MAX_RADIUS - radius + 1),
            color=Color.all_random(),
            radius=radius
        )

    def __init__(self, pos: Position, radius: float, color: Color):
        self.__pos = pos
        self.__radius = radius
        self.__color = color
        self.__diff = (Star.MAX_RADIUS - self.__radius + 1)
        self.__diff_pos = Position(GAME_FIELD_RECT.width, GAME_FIELD_RECT.height) * self.__diff / Star.MAX_RADIUS / 2

    def draw(self, sc: pygame.Surface, camera: CameraABC):
        screen_pos = camera.get_screen_pos(self.__pos)
        screen_pos = screen_pos / self.__diff + self.__diff_pos
        pygame.draw.rect(
            sc,
            self.__color,
            (screen_pos.x, screen_pos.y, self.__radius * 2, self.__radius * 2)
        )
