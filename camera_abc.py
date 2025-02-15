
from abc import ABC, abstractmethod
from typing import Tuple
from pygame import Rect
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH
from position import Position


class CameraABC(ABC):
    ...

    @abstractmethod
    def get_camera_pos(self) -> Tuple[float, float]: ...

    def get_screen_pos(self, object_pos: Rect | Tuple[int, int]) -> Position:
        camera_pos = self.get_camera_pos()

        camera_x = camera_pos[0] - HALF_SCREEN_WIDTH
        camera_y = camera_pos[1] - HALF_SCREEN_HEIGHT

        if isinstance(object_pos, Rect):
            obj_x = object_pos.x
            obj_y = object_pos.y
        elif isinstance(object_pos, tuple):
            obj_x = object_pos[0]
            obj_y = object_pos[1]
        else:
            raise Exception("Unsupported object_pos type.")

        screen_pos_x = obj_x - camera_x
        screen_pos_y = obj_y - camera_y

        return Position(screen_pos_x, screen_pos_y)
