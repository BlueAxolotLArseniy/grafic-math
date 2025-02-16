import pygame
import math
from bullet_affiliation import BulletAffiliation
from bullets import Bullets
from camera_abc import CameraABC
from enemy_type import EnemyType

from common import draw_text, get_angle_to_player, rotate_image
from consts import BLACK, DUMMY_ENEMIES, MOVE_ENEMY_WITH_ONE_BARREL_SPEED, MOVE_ENEMY_WITH_TWO_BARREL_SPEED, BASE_ENEMY_HEALTH, RED
from bullet import Bullet
from player import Player
from position import Position
from game_state import GameState


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos: Position, player: Player, setting_type: EnemyType, game_state: GameState, bullets: Bullets):

        self.game_state = game_state

        self.start_pos = pos

        if setting_type == EnemyType.single_cannon:
            self.rate_of_fire = 10
            self.speed = MOVE_ENEMY_WITH_ONE_BARREL_SPEED
            self.image = pygame.image.load('images/game_textures/enemy1barrels.png').convert()
            self.start_health = BASE_ENEMY_HEALTH * 1.5

        if setting_type == EnemyType.double_cannon:
            self.rate_of_fire = 14
            self.speed = MOVE_ENEMY_WITH_TWO_BARREL_SPEED
            self.image = pygame.image.load('images/game_textures/enemy2barrels.png').convert()
            self.start_health = BASE_ENEMY_HEALTH

        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=pos)

        self.player = player
        self.__bullets = bullets

        self.respawn()

    def respawn(self):
        self.time = 0
        self.__angle = 0
        self.health = self.start_health
        self.rect.center = self.start_pos

    def _rotate(self):
        self.__angle = get_angle_to_player(
            self.rect.centerx,
            self.rect.centery,
            self.player.rect.centerx,
            self.player.rect.centery
        )
        self.image, self.rect = rotate_image(self.original_image, self.rect.center, self.__angle)

    def update(self):
        if self.health < 0:
            return

        self.time += 1

        self._rotate()

        self.rect.centerx += int(self.speed * math.cos(self.__angle))
        self.rect.centery += int(self.speed * math.sin(self.__angle))

        if not DUMMY_ENEMIES:
            if self.time % self.rate_of_fire == 0:
                bullet = Bullet(self.__angle, Position.from_tuple(self.rect.center),
                                BulletAffiliation.enemy, 1, self.game_state)
                self.__bullets.append(bullet)

        for bullet in self.__bullets.collide_with(self.rect, BulletAffiliation.player):
            self.health -= 1 * bullet.koefficient

    def draw(self, sc: pygame.Surface, camera: CameraABC):
        if self.health < 0:
            return
        screen_pos = camera.get_screen_pos(self.rect)
        sc.blit(self.image, screen_pos)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, RED, (*screen_pos, self.rect.width, self.rect.height), 2)
            draw_text(sc, f'x={self.rect.centerx}, y={self.rect.centery}', screen_pos + Position(0, -20))
