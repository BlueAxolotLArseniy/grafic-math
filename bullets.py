
from typing import Generator, List
from pygame import Rect, Surface
from bullet import Bullet
from bullet_affiliation import BulletAffiliation
from camera_abc import CameraABC
from consts import BULLET_MAX_DISTANCE
from game_state import GameState


class Bullets:

    def __init__(self, game_state: GameState):
        self.__bullets: List[Bullet] = []
        self.__game_state = game_state

    def draw(self, sc: Surface, camera: CameraABC):
        for bullet in self.__bullets:
            bullet.draw(sc, camera, self.__game_state.debug_mode)

    def update(self):

        for num, bullet in enumerate(self.__bullets):
            bullet.update()
            if bullet.distance > BULLET_MAX_DISTANCE:
                self.__bullets.pop(num)

    def collide_with(self, rect: Rect, bullet_affiliation: BulletAffiliation) -> Generator[Bullet, None, None]:
        for bullet in self.__bullets:
            if bullet.affiliation == bullet_affiliation and rect.colliderect(bullet.get_rect()):
                yield bullet

    def append(self, bullet: Bullet):
        self.__bullets.append(bullet)

    def count(self) -> int:
        return len(self.__bullets)

    def remove(self, bullet: Bullet):
        self.__bullets.remove(bullet)
