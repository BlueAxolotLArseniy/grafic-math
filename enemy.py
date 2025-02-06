import pygame
import math
import player

from common import get_angle_to_player, rotate_image
from consts import BLACK, MOVE_ENEMY_WITH_ONE_BARREL_SPEED, MOVE_ENEMY_WITH_TWO_BARREL_SPEED, BASE_ENEMY_HEALTH, RED
from bullet import Bullet
from state import GameState


class Enemy(pygame.sprite.Sprite):

    def __init__(self, x: int | float, y: int | float, player: player.Player, setting: str, game_state: GameState):
        setting_type = setting

        self.game_state = game_state

        if setting_type == 'WithOneBarrel':
            self.rate_of_fire = 10
            self.speed = MOVE_ENEMY_WITH_ONE_BARREL_SPEED
            self.image = pygame.image.load('images/game_textures/enemy1barrels.png').convert()
            self.health = BASE_ENEMY_HEALTH * 1.5

        if setting_type == 'WithTwoBarrels':
            self.rate_of_fire = 14
            self.speed = MOVE_ENEMY_WITH_TWO_BARREL_SPEED
            self.image = pygame.image.load('images/game_textures/enemy2barrels.png').convert()
            self.health = BASE_ENEMY_HEALTH

        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(x, y))

        self.player = player

        self.__angle = get_angle_to_player(self.rect.centerx, self.rect.centery,
                                           self.player.rect.centerx, self.player.rect.centery)
        self.time = 0

    def _rotate(self):
        self.__angle = get_angle_to_player(
            self.rect.centerx,
            self.rect.centery,
            self.player.rect.centerx,
            self.player.rect.centery
        )

        self.image, self.rect = rotate_image(self.original_image, self.rect.center, self.__angle)

    def update(self, kx, ky):
        if self.health < 0:
            return

        self.time += 1

        self._rotate()

        self.rect.centerx += int(self.speed * math.cos(self.__angle))
        self.rect.centery += int(self.speed * math.sin(self.__angle))

        if self.time % self.rate_of_fire == 0:
            bullet = Bullet(self.__angle, self.rect.center, True, 1, self.game_state)
            self.player.bullets.append(bullet)

        self.rect.x += kx
        self.rect.y += ky

        for b in self.player.bullets:
            if self.rect.colliderect(b.rect) and b.affiliation != False:
                self.health -= 1 * b.koefficient

    def draw(self, sc: pygame.Surface):
        if self.health < 0:
            return

        sc.blit(self.image, self.rect)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, RED, self.rect, 2)
