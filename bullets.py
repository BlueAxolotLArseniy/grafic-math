
from typing import Generator, List

from pygame import Rect, Surface
from bullet import Bullet
from bullet_affiliation import BulletAffiliation

from camera_abc import CameraABC
from consts import SCREEN_HEIGHT, SCREEN_WIDTH


class Bullets:

    def __init__(self):
        self.__bullets: List[Bullet] = []

    def draw(self, sc: Surface, camera: CameraABC):
        for bullet in self.__bullets:
            bullet.draw(sc, camera)

    def update(self):

        for bullet in self.__bullets:
            bullet.update()

        for num in range(len(self.__bullets)-1):
            bullet = self.__bullets[num]
            if bullet.rect.centerx > SCREEN_WIDTH + bullet.rect.width or bullet.rect.centerx < 0 - bullet.rect.width:
                self.__bullets.pop(num)
                break
            if bullet.rect.centery > SCREEN_HEIGHT + bullet.rect.height or bullet.rect.centery < 0 - bullet.rect.height:
                self.__bullets.pop(num)
                break

    def collide_with(self, rect: Rect, bullet_affiliation: BulletAffiliation) -> Generator[Bullet, None, None]:
        for bullet in self.__bullets:
            if bullet.affiliation == bullet_affiliation and rect.colliderect(bullet.rect):
                yield bullet

    def append(self, bullet: Bullet):
        self.__bullets.append(bullet)

    def count(self) -> int:
        return len(self.__bullets)
