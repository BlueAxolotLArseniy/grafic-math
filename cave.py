import pygame

from consts import BLACK, WHITE
from state import GameState


class Cave(pygame.sprite.Sprite):
    def __init__(self, x, y, game_state: GameState):
        self.image = pygame.image.load('images/game_textures/cave.png').convert()
        self.image.set_colorkey(BLACK)
        self.original_image = self.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*15, self.image.get_height()*15))

        self.rect = self.image.get_rect(center=(x, y))

        self.game_state = game_state

    def update(self, kx, ky):
        self.rect.x += kx
        self.rect.y += ky

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, WHITE, self.rect, 2)
