import pygame
import math
import common
import consts
import player
import bullet

class Enemy(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, player: player.Player):
        self.speed = consts.MOVE_PLAYER_SPEED-3
        
        self.image = pygame.image.load('images/enemy.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image
        
        self.rect = self.image.get_rect(center=(x, y))
        
        self.player = player
        
        self.__angle = common.get_angle_to_player(self.rect.centerx, self.rect.centery,
                                self.player.rect.centerx, self.player.rect.centery)
        self.time = 0

    def _rotate(self):
        self.__angle = common.get_angle_to_player(self.rect.centerx, self.rect.centery,
                        self.player.rect.centerx, self.player.rect.centery)
        
        self.image = pygame.transform.rotate(self.original_image, int(common.radians_to_degrees(-self.__angle)))
        
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):
        global bullet
        
        self.time += 1
        
        self._rotate()
        
        self.rect.centerx += int(self.speed * math.cos(self.__angle))
        self.rect.centery += int(self.speed * math.sin(self.__angle))
        
        if self.time % 3 == 0:
            
            bullet = bullet.Bullet(self.__angle, self.rect.centerx, self.rect.centery)
            self.player.bullets.append(bullet)

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)
