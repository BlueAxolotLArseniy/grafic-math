from typing import Tuple
import pygame

from bullet import Bullet
from bullet_affiliation import BulletAffiliation
from bullets import Bullets
from camera_abc import CameraABC
from common import draw_text, get_angle_to_mouse, rotate_image
from consts import BASE_PLAYER_HEALTH, GREEN, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, ORANGE, YELLOW, RED
import consts
from position import Position
from state import GameState
import ui.death_screen as ds


class Player(CameraABC):
    def __init__(self, x, y, game_state: GameState, bullets: Bullets):
        self.image = pygame.image.load('images/game_textures/ship.png').convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(x, y))
        self.original_rect = self.rect.copy()

        self.time = 0

        self.__bullets = bullets

        self.health = BASE_PLAYER_HEALTH

        self.game_state = game_state

        self.kx = 0
        self.ky = 0

    def _rotate(self):
        x, y = self.get_screen_pos(self.rect)
        self.angle = get_angle_to_mouse(x, y)
        self.image, self.rect = rotate_image(self.original_image, self.rect.center, self.angle)

    def update(self):
        self.time += 1
        self._rotate()
        self.__move_player()

        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.time % 4 == 0:
            if left:
                bullet = Bullet(self.angle, self.rect.center, BulletAffiliation.player, 1, self.game_state)
                self.__bullets.append(bullet)

        for bullet in self.__bullets.collide_with(self.rect, BulletAffiliation.enemy):
            self.health -= 1 * bullet.koefficient

        if self.health <= 0:
            self.game_state.active_screen = ds.DeathScreen(self.game_state)

    def __move_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.ky = consts.MOVE_PLAYER_SPEED
        elif keys[pygame.K_w]:
            self.ky = -consts.MOVE_PLAYER_SPEED
        else:
            # Если клавиша не нажата, замедляем движение
            self.ky *= 0.9  # Коэффициент замедления (чем меньше, тем плавнее остановка)

        if keys[pygame.K_d]:
            self.kx = -consts.MOVE_PLAYER_SPEED
        elif keys[pygame.K_a]:
            self.kx = consts.MOVE_PLAYER_SPEED
        else:
            self.kx *= 0.9  # Замедление по оси X

        # Останавливаем игрока, если скорость становится очень маленькой
        if abs(self.kx) < 0.1:
            self.kx = 0
        if abs(self.ky) < 0.1:
            self.ky = 0

        self.rect.centerx -= int(self.kx)
        self.rect.centery += int(self.ky)

    def draw_hp(self, sc):
        # todo: move hp to a separate class.
        pygame.draw.rect(sc, WHITE, (19, SCREEN_HEIGHT-19-22, 202, 22), 1)
        if self.health >= 75:
            pygame.draw.rect(sc, GREEN, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))
        elif self.health >= 50:
            pygame.draw.rect(sc, YELLOW, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))
        elif self.health >= 25:
            pygame.draw.rect(sc, ORANGE, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))
        elif self.health >= 0:
            pygame.draw.rect(sc, RED, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))

    def draw(self, sc: pygame.Surface):

        screen_pos = self.get_screen_pos(self.rect)
        sc.blit(self.image, tuple(screen_pos))

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, WHITE, (screen_pos.x, screen_pos.y, self.rect.width, self.rect.height), 2)
            # tod, here will be move of the pos.
            draw_text(
                sc,
                f'x={self.rect.centerx}, y={self.rect.centery}',
                Position(HALF_SCREEN_WIDTH - 40, HALF_SCREEN_HEIGHT + 60)
            )

        self.draw_hp(sc)

    def get_camera_pos(self) -> Tuple[float, float]:
        return self.rect.centerx, self.rect.centery
