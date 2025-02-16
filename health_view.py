

from typing import Tuple
import pygame

from common import draw_text
from consts import GREEN, ORANGE, RED, WHITE, YELLOW
from position import Position


class HealthView:

    def __init__(self, max_health: float, scale: int = 1):
        self.__width = 50*scale
        self.__height = 5*scale
        self.__max_health = max_health
        self.font = pygame.font.Font('fonts/Monocraft.otf', round(5 + 5*scale))

    def draw(self, sc: pygame.Surface, health: float, pos: Position, text_draw: bool = False):
        pygame.draw.rect(sc, WHITE, (pos.x-1, pos.y-1, self.__width+1, self.__height+1), 1)

        color = self.__get_color(health)
        pygame.draw.rect(sc, color, (pos.x, pos.y, self.__width*health//self.__max_health, self.__height))

        if text_draw:
            draw_text(sc, f'HP {health:.0f}', pos + Position(0, -self.__height*1.5), WHITE, self.font)

    def __get_color(self, health: float) -> Tuple[int, int, int]:
        if health >= 75:
            return GREEN
        elif health >= 50:
            return YELLOW
        elif health >= 25:
            return ORANGE

        return RED
