import pygame
import math
import common
import consts
import player
from bullet import Bullet

class Enemy():
    
    class WithOneBarrels(pygame.sprite.Sprite):

        def __init__(self, x: int, y: int, player: player.Player):
            self.speed = consts.MOVE_ENEMY_WITH_ONE_BARREL_SPEED
            
            self.image = pygame.image.load('images/enemy1barrels.png').convert()
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
            
            self.time += 1
            
            self._rotate()
            
            self.rect.centerx += int(self.speed * math.cos(self.__angle))
            self.rect.centery += int(self.speed * math.sin(self.__angle))
            
            if self.time % 5 == 0:
                
                bullet = Bullet(self.__angle, self.rect.center, True, 1)
                self.player.bullets.append(bullet)

        def draw(self, sc: pygame.Surface):
            sc.blit(self.image, self.rect)
            
            if consts.DEBUG_MODE:
                pygame.draw.rect(sc, (255, 0, 0), self.rect, 2)

    class WithTwoBarrels(pygame.sprite.Sprite):

        def __init__(self, x: int, y: int, player: player.Player):
            self.speed = consts.MOVE_ENEMY_WITH_TWO_BARREL_SPEED
            
            self.image = pygame.image.load('images/enemy2barrels.png').convert()
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
            
        def get_rotated_topleft(self, image, rect, angle):
            # Центр прямоугольника
            center_x, center_y = rect.center

            # Смещение topleft относительно центра
            offset_x = rect.topleft[0] - center_x
            offset_y = rect.topleft[1] - center_y

            # Угол в радианах
            angle_rad = math.radians(angle)

            # Вычисляем новые координаты
            new_x = center_x + math.cos(angle_rad) * offset_x - math.sin(angle_rad) * offset_y
            new_y = center_y + math.sin(angle_rad) * offset_x + math.cos(angle_rad) * offset_y

            return (new_x, new_y)

        def update(self):
            
            self.time += 1
            
            self._rotate()
            
            self.rect.centerx += int(self.speed * math.cos(self.__angle))
            self.rect.centery += int(self.speed * math.sin(self.__angle))
            
            if self.time % 7 == 0:
                
                # bullet = Bullet(self.__angle, self.get_rotated_topleft(self.image, self.rect, self.__angle))
                bullet = Bullet(self.__angle, self.rect.center, True, 3)
                self.player.bullets.append(bullet)

        def draw(self, sc: pygame.Surface):
            sc.blit(self.image, self.rect)
            
            if consts.DEBUG_MODE:
                pygame.draw.rect(sc, (255, 0, 0), self.rect, 2)

