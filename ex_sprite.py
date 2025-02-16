from typing import Tuple
import pygame
from common import radians_to_degrees
from consts import BACKGROUND_COLOR
from image_loader import ImageLoader
from position import Position


class ExSprite(pygame.sprite.Sprite):

    def __init__(self, image_path: str, angle: float = 0, scale: float = 1.0, color_key: Tuple[int, int, int] | None = None):
        super().__init__()

        image = ImageLoader.get_image(image_path).convert()

        if color_key:
            image.set_colorkey(color_key)

        self.image = pygame.transform.scale(image, (image.get_width()*scale, image.get_height()*scale))

        self.__angle = 0
        self.angle = angle

    @property
    def angle(self):
        return self.__angle

    @angle.setter
    def angle(self, value):
        if not self.__angle or self.__angle != value:
            self.__angle = value
            self.__rotated_image = pygame.transform.rotate(self.image, radians_to_degrees(-self.__angle))

    def get_rotated_rect(self, position: Position):
        return self.__rotated_image.get_rect(center=position)

    def draw(self, screen: pygame.Surface, position: Position, debug_info: bool):
        rotated_rect = self.get_rotated_rect(position)

        screen.blit(self.__rotated_image, rotated_rect.topleft)
        if debug_info:
            pygame.draw.circle(screen, (200, 0, 0), rotated_rect.topleft, 10, 1)
            pygame.draw.circle(screen, (0, 220, 0), rotated_rect.center, 10, 1)
            pygame.draw.rect(screen, (220, 220, 220), rotated_rect, 1)
            pygame.draw.circle(screen, (100, 220, 150), (position.x, position.y), 6.0, 1)

    def draw_background(self, screen: pygame.Surface, position: Position):
        size = 100
        rect = self.get_rotated_rect(position)
        new_width = rect.width + size
        new_height = rect.height + size
        new_x = rect.x - size / 2
        new_y = rect.y - size / 2
        rect = pygame.Rect(new_x, new_y, new_width, new_height)
        pygame.draw.rect(screen, BACKGROUND_COLOR, rect)  # (new_x, new_y, new_width, new_height))
