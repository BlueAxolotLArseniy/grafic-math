from pygame import Surface
import pygame
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from state import GameState


class Blur:

    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.blur_sc = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

    def update(self, event):
        ...

    def draw(self, sc: Surface,):
        if self.game_state.is_paused:
            self.blur_sc.fill((0, 0, 0))
            self.blur_sc.set_alpha(200)
            sc.blit(self.blur_sc, (0, 0))
