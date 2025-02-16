import pygame

from camera_abc import CameraABC
from common import draw_text
from consts import BLACK, WHITE
from game_state import GameState


class Cave(pygame.sprite.Sprite):
    def __init__(self, x, y, game_state: GameState):
        self.image = pygame.image.load('images/game/cave.png').convert()
        self.image.set_colorkey(BLACK)
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*15, self.image.get_height()*15))

        self.rect = self.image.get_rect(center=(x, y))

        self.game_state = game_state

    def update(self): ...

    def draw(self, sc: pygame.Surface, camera: CameraABC):
        screen_pos = camera.get_screen_pos(self.rect)
        sc.blit(self.image, screen_pos)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, WHITE, (*screen_pos, self.rect.width, self.rect.height), 2)
            draw_text(sc, f'x={self.rect.centerx}, y={self.rect.centery}', screen_pos)
