import pygame
import math
import common
import consts
import player
from bullet import Bullet


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, player: player.Player, setting: str):
        setting_type = setting

        self.x_speed = 0
        self.y_speed = 0

        if setting_type == 'WithOneBarrel':
            self.rate_of_fire = 5
            self.speed = consts.MOVE_ENEMY_WITH_ONE_BARREL_SPEED

            self.image = pygame.image.load('images/enemy1barrels.png').convert()

        if setting_type == 'WithTwoBarrels':
            self.rate_of_fire = 7
            self.speed = consts.MOVE_ENEMY_WITH_TWO_BARREL_SPEED

            self.image = pygame.image.load('images/enemy2barrels.png').convert()

        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(x, y))

        self.player = player

        self.__angle = common.get_angle_to_player(self.rect.centerx, self.rect.centery,
                                                  self.player.rect.centerx, self.player.rect.centery)
        self.time = 0

    def _rotate(self):
        self.__angle = common.get_angle_to_player(
            self.rect.centerx,
            self.rect.centery,
            self.player.rect.centerx,
            self.player.rect.centery
        )
        self.image, self.rect = common.rotate_image(self.original_image, self.rect.center, self.__angle)

    def update(self):

        self.time += 1

        self._rotate()

        self.rect.centerx += int(self.speed * math.cos(self.__angle))
        self.rect.centery += int(self.speed * math.sin(self.__angle))

        if self.time % self.rate_of_fire == 0:

            bullet = Bullet(self.__angle, self.rect.center, True, 1)
            self.player.bullets.append(bullet)

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)

        if consts.DEBUG_MODE:
            pygame.draw.rect(sc, (255, 0, 0), self.rect, 2)
