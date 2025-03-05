from typing import List

from pygame import Surface

from camera_abc import CameraABC
from consts import HALF_SCREEN_HEIGHT, HALF_SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_WIDTH
from player import Player
from position import Position
from star_chunk import StarChunk
from stars import Stars

class StarChunks:
    def __init__(self, player: Player):
        self.__chunks = {'TR': StarChunk(Stars(), Position(HALF_SCREEN_WIDTH, 0-HALF_SCREEN_HEIGHT), self.player), 
                         'TL': StarChunk(Stars(), Position(0-HALF_SCREEN_WIDTH, 0-HALF_SCREEN_HEIGHT), self.player), 
                         'BR': StarChunk(Stars(), Position(HALF_SCREEN_WIDTH, 0+HALF_SCREEN_HEIGHT), self.player), 
                         'BL': StarChunk(Stars(), Position(0-HALF_SCREEN_WIDTH, 0+HALF_SCREEN_HEIGHT), self.player)}
        
        self.player = player
    
    def draw(self, sc: Surface, cam: CameraABC):
        for chunk in self.__chunks.values():
            chunk.draw(sc, cam)
    
    def update(self):
        self.__move_chunks()
    
    def __move_chunks(self):
        if self.player.position.x > self.__chunks['TR'].__rect.centerx:
            self.__move_right()
        elif self.player.position.x < self.__chunks['TL'].__rect.centerx:
            self.__move_left()
            
        if self.player.position.y < self.__chunks['TR'].__rect.centery:
            self.__move_up()
        elif self.player.position.y > self.__chunks['BR'].__rect.centery:
            self.__move_down()
                
    def __change_horizontal_keys(self):
        self.__chunks['TR'], self.__chunks['TL'] = self.__chunks['TL'], self.__chunks['TR']
        self.__chunks['BR'], self.__chunks['BL'] = self.__chunks['BL'], self.__chunks['BR']
    
    def __change_vertical_keys(self):
        self.__chunks['TR'], self.__chunks['BR'] = self.__chunks['BR'], self.__chunks['TR']
        self.__chunks['TL'], self.__chunks['BL'] = self.__chunks['BL'], self.__chunks['TL']
    
    def __move_left(self):
        self.__chunks['TR'].__rect.centerx -= SCREEN_WIDTH
        self.__chunks['BR'].__rect.centerx -= SCREEN_WIDTH

        self.__change_horizontal_keys()
    
    def __move_right(self):
        self.__chunks['TL'].__rect.centerx += SCREEN_WIDTH
        self.__chunks['BL'].__rect.centerx += SCREEN_WIDTH

        self.__change_horizontal_keys()
    
    def __move_up(self):
        self.__chunks['BR'].__rect.centery -= SCREEN_HEIGHT
        self.__chunks['BL'].__rect.centery -= SCREEN_HEIGHT
        
        self.__change_vertical_keys()
    
    def __move_down(self):
        self.__chunks['TR'].__rect.centery += SCREEN_HEIGHT
        self.__chunks['TL'].__rect.centery += SCREEN_HEIGHT
        
        self.__change_vertical_keys()