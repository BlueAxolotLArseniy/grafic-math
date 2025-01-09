import pygame
import math
from common import radians_to_degrees, get_angle_to_player
from consts import MOVE_PLAYER_SPEED, BULLET_SPEED
from player import Player
from bullet import Bullet



class Enemy(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, player: Player):
        self.speed = MOVE_PLAYER_SPEED-3
        self.image = pygame.image.load('images/enemy.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image
        self.rect = self.image.get_rect(center=(x, y))
        self.player = player
        self.__angle = get_angle_to_player(self.rect.centerx, self.rect.centery,
                                self.player.rect.centerx, self.player.rect.centery)
        self.time = 0

    def _rotate(self):
        self.__angle = get_angle_to_player(self.rect.centerx, self.rect.centery,
                        self.player.rect.centerx, self.player.rect.centery)
        self.image = pygame.transform.rotate(self.original_image, int(radians_to_degrees(-self.__angle)))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):
        self.time += 1
        self._rotate()
        self.delta_x = int(self.speed * math.cos(self.__angle))
        self.delta_y = int(self.speed * math.sin(self.__angle))
        self.rect.centerx += self.delta_x
        self.rect.centery += self.delta_y
        
        if self.time % 3 == 0:
            bullet = Bullet(self.__angle, BULLET_SPEED, self.rect.centerx, self.rect.centery)
            self.player.bullets.append(bullet)

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)
