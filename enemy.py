import pygame
import math
from bullet_affiliation import BulletAffiliation
from bullets import Bullets
from camera_abc import CameraABC
from enemy_settings import EnemySettings
from common import draw_text, get_angle_to_player
from consts import BLACK, DUMMY_ENEMIES
from bullet import Bullet
from ex_sprite import ExSprite
from health_view import HealthView
from player import Player
from position import Position
from game_state import GameState


class Enemy(pygame.sprite.Sprite):

    def __init__(self, pos: Position, player: Player, enemy_settings: EnemySettings, game_state: GameState, bullets: Bullets):

        self.game_state = game_state
        self.player = player
        self.__bullets = bullets

        self.start_pos = pos
        self.__enemy_settings = enemy_settings

        self.sprite = ExSprite(enemy_settings.image_path, scale=5, color_key=BLACK)

        self.__health_view = HealthView(enemy_settings.health)

        self.respawn()

    def respawn(self):
        self.time = 0
        self.__angle = 0
        self.health = self.__enemy_settings.health
        self.position = self.start_pos

    def _rotate(self):
        self.__angle = get_angle_to_player(
            self.position.x,
            self.position.y,
            self.player.position.x,
            self.player.position.y
        )
        self.sprite.angle = self.__angle

    def update(self):
        if self.health < 0:
            return

        self.time += 1

        self._rotate()

        delta_pos = Position(
            self.__enemy_settings.speed * math.cos(self.__angle),
            self.__enemy_settings.speed * math.sin(self.__angle)
        )
        self.position += delta_pos

        if not DUMMY_ENEMIES:
            if self.time % self.__enemy_settings.fire_rate == 0:
                bullet = Bullet(self.__angle, self.position, BulletAffiliation.enemy,
                                self.__enemy_settings.bullet_damage, self.__enemy_settings.bullet_speed, delta_pos)
                self.__bullets.append(bullet)

        for bullet in self.__bullets.collide_with(self.sprite.get_rotated_rect(self.position), BulletAffiliation.player):
            self.health -= 1 * bullet.damage
            self.__bullets.remove(bullet)

    def draw(self, sc: pygame.Surface, camera: CameraABC):
        if self.health < 0:
            return

        screen_pos = camera.get_screen_pos(self.position)
        self.sprite.draw(sc, screen_pos, self.game_state.debug_mode)

        if self.game_state.debug_mode:
            draw_text(sc, f'game: {self.position}', screen_pos + Position(0, -20))

        self.__health_view.draw(sc, self.health, screen_pos + Position(-25, 47))
