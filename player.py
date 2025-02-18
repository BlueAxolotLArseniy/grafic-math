from typing import Tuple
import pygame
from bullet import Bullet
from bullet_affiliation import BulletAffiliation
from bullets import Bullets
from camera_abc import CameraABC
from common import draw_text, get_angle_to_mouse
from consts import BASE_PLAYER_HEALTH, GREEN, HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, ORANGE, YELLOW, RED
import consts
from ex_sprite import ExSprite
from health_view import HealthView
from position import Position
from game_state import GameState
import ui.death_screen as ds


class Player(CameraABC):
    def __init__(self, pos: Position, game_state: GameState, bullets: Bullets):

        self.sprite = ExSprite('images/game/ship.png', scale=5, color_key=BLACK)

        self.start_pos = pos

        self.start_health = BASE_PLAYER_HEALTH

        self.__screen_pos = Position(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT)

        self.__bullets = bullets
        self.game_state = game_state

        self.__health_view = HealthView(self.start_health, scale=4)

        self.respawn()

    def respawn(self):
        self.x_change = 0
        self.y_change = 0
        self.time = 0
        self.health = self.start_health
        self.position = self.start_pos

    def update(self):
        self.time += 1

        self.sprite.angle = get_angle_to_mouse(self.__screen_pos.x, self.__screen_pos.y)

        self.__move_player()

        keys = pygame.key.get_pressed()

        left, middle, right = pygame.mouse.get_pressed()
        if self.time % 4 == 0:
            if left or keys[pygame.K_SPACE]:
                bullet = Bullet(self.sprite.angle, self.position, BulletAffiliation.player,
                                1, delta_speed=Position(self.x_change, self.y_change))
                self.__bullets.append(bullet)

        for bullet in self.__bullets.collide_with(self.sprite.get_rotated_rect(self.position), BulletAffiliation.enemy):
            self.health -= 1 * bullet.damage

        if self.health <= 0:
            self.game_state.active_screen = ds.DeathScreen(self.game_state)

    def __move_player(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_s]:
            self.y_change = consts.MOVE_PLAYER_SPEED
        elif keys[pygame.K_w]:
            self.y_change = -consts.MOVE_PLAYER_SPEED
        else:
            # Если клавиша не нажата, замедляем движение
            self.y_change *= 0.9  # Коэффициент замедления (чем меньше, тем плавнее остановка)

        if keys[pygame.K_d]:
            self.x_change = consts.MOVE_PLAYER_SPEED
        elif keys[pygame.K_a]:
            self.x_change = -consts.MOVE_PLAYER_SPEED
        else:
            self.x_change *= 0.9  # Замедление по оси X

        # Останавливаем игрока, если скорость становится очень маленькой
        if abs(self.x_change) < 0.1:
            self.x_change = 0
        if abs(self.y_change) < 0.1:
            self.y_change = 0

        self.position += Position(self.x_change, self.y_change)

    def draw(self, sc: pygame.Surface):

        self.sprite.draw(sc, self.__screen_pos, self.game_state.debug_mode)

        if self.game_state.debug_mode:

            # todo here will be move of the pos.
            draw_text(
                sc,
                f'game: {self.position}',
                Position(HALF_SCREEN_WIDTH - 40, HALF_SCREEN_HEIGHT + 60)
            )

            draw_text(
                sc,
                f'sc: x={self.__screen_pos.x}, y={self.__screen_pos.y}',
                Position(HALF_SCREEN_WIDTH - 40, HALF_SCREEN_HEIGHT + 40)
            )

            mouse_pos = pygame.mouse.get_pos()

            draw_text(
                sc,
                f'sc: x={mouse_pos[0]}, y={mouse_pos[1]}',
                Position(mouse_pos[0]+20, mouse_pos[1])
            )

        self.__health_view.draw(sc, self.health, Position(20, SCREEN_HEIGHT-41), True)

    def get_camera_pos(self) -> Tuple[float, float]:
        return self.position
