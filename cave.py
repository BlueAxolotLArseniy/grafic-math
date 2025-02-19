import pygame

from camera_abc import CameraABC
from common import draw_text
from consts import BLACK, WHITE
from game_state import GameState
from player import Player


class Cave(pygame.sprite.Sprite):
    def __init__(self, x, y, game_state: GameState, player: Player):

        self.image = pygame.image.load('images/game/cave.png').convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*15, self.image.get_height()*15))

        self.rect = self.image.get_rect(center=(x, y))

        self.__player = player

        self.game_state = game_state

    def update(self):
        if self.__player.sprite.get_rotated_rect(self.__player.position).colliderect(self.rect):
            if not self.__player.health >= self.__player.start_health:
                self.__player.health += 1

    def draw(self, sc: pygame.Surface, camera: CameraABC):
        screen_pos = camera.get_screen_pos(self.rect)
        sc.blit(self.image, screen_pos)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, WHITE, (*screen_pos, self.rect.width, self.rect.height), 2)
            draw_text(sc, f'x={self.rect.centerx}, y={self.rect.centery}', screen_pos)
