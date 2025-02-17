

from typing import List

from pygame import Surface
from camera_abc import CameraABC
from star import Star


class Stars:

    @classmethod
    def random(cls, count) -> 'Stars':
        stars = Stars()
        for _ in range(count):
            stars.append(Star.random())
        return stars

    def __init__(self):
        self.__stars: List[Star] = []

    def append(self, star: Star):
        self.__stars.append(star)

    def draw(self, sc: Surface, camera: CameraABC):
        for star in self.__stars:
            star.draw(sc, camera)
