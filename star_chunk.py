from pygame import Rect, Surface
from camera_abc import CameraABC
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from position import Position
from stars import Stars


class StarChunk:
    def __init__(self, stars: Stars, pos: Position, player: Player):
        self.__stars = stars
        
        self.player = player
        
        self.__pos = pos
        self.__rect = Rect(self.__pos.x, self.__pos.y, SCREEN_WIDTH, SCREEN_HEIGHT)
        
        self.__stars.random(25, self.__rect)
    
    def draw(self, sc: Surface, cam: CameraABC):
        self.__stars.draw(sc, cam)
