from typing import List

from pygame import Surface

from camera_abc import CameraABC
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH
from player import Player
from position import Position
from star_chunk import StarChunk
from stars import Stars




class StarChunks:
    def __init__(self, player: Player):
        # self.__chunks = {'BR': }
        self.player = player
    
    def draw(self, sc: Surface, cam: CameraABC):
        for chunk in self.__chunks:
            # chunk.draw(sc, cam)
            ...
    
    def update(self):
        ...
