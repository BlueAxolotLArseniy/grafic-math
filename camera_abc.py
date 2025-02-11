
from abc import ABC, abstractmethod
from typing import Tuple
from pygame import Rect
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH


class CameraABC(ABC):
    ...

    @abstractmethod
    def get_camera_pos(self) -> Tuple[float, float]: ...

    def get_screen_pos(self, object_pos: Rect) -> Tuple[float, float]:
        camera_pos = self.get_camera_pos()

        camera_x = camera_pos[0] - HALF_SCREEN_WIDTH
        camera_y = camera_pos[1] - HALF_SCREEN_HEIGHT

        screen_pos_x = object_pos.centerx - camera_x
        screen_pos_y = object_pos.centery - camera_y

        return (screen_pos_x, screen_pos_y)
