import math
from typing import Tuple
import pygame
from pygame.font import Font
from consts import GREEN
from position import Position


def radians_to_degrees(radians: float):
    return (180 / math.pi) * radians


def get_angle_to_mouse(x, y):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    rel_x, rel_y = mouse_x - x, mouse_y - y
    return math.atan2(rel_y, rel_x)


def get_angle_to_player(x, y, playerx, playery):
    rel_x, rel_y = playerx - x, playery - y
    return math.atan2(rel_y, rel_x)


def rotate_image(original_image, center, angle):
    image = pygame.transform.rotate(original_image, int(radians_to_degrees(-angle)))
    rect = image.get_rect(center=center)
    return (image, rect)


def draw_text(sc: pygame.Surface, text: str, screen_pos: Position, font_size: int = 20, color: Tuple[int, int, int] = GREEN):
    font = Font(None, font_size)
    text_render = font.render(text, False, color)
    sc.blit(text_render, screen_pos)
