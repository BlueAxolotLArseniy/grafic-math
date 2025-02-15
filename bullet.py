import pygame
import math

from bullet_affiliation import BulletAffiliation
from camera_abc import CameraABC
from common import draw_text, rotate_image
from consts import BLACK, BULLET_SPEED, GREEN
from position import Position
from state import GameState


class Bullet(pygame.sprite.Sprite):
    def __init__(self, angle: float, pos: Position, affiliation: BulletAffiliation, koefficient: float, game_state: GameState):

        image = pygame.image.load('images/game_textures/ship.png').convert()
        image.set_colorkey(BLACK)

        self.image, self.rect = rotate_image(image, pos, angle)

        self.pos = pos
        self.delta_pos = Position(BULLET_SPEED * math.cos(angle), BULLET_SPEED * math.sin(angle))

        self.affiliation = affiliation
        self.koefficient = koefficient

        self.game_state = game_state

        self.distance = 0

    def update(self):
        self.pos += self.delta_pos
        self.distance += BULLET_SPEED

    def draw(self, sc: pygame.Surface, camera: CameraABC):
        screen_pos = camera.get_screen_pos(self.pos)
        sc.blit(self.image, screen_pos)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, GREEN, (*screen_pos, self.rect.width, self.rect.height), 2)
            draw_text(sc, f'x={self.pos.x:.0f}, y={self.pos.y:.0f}', screen_pos + Position(0, -20))
