import pygame
import random
import math
from contstants import MOVE_PLAYER_SPEED
pygame.init()

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.real_time = 0
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))#a
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()
        self.x_speed = 0
        self.y_speed = 0
        
    def rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(angle))
        self.rect = self.image.get_rect(center=(self.x, self.y))
    
    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.last_key = event.key

        self.real_time += 1
        
        # Проверяем нажатия клавиш
        if keys[pygame.K_w]:
            self.y_speed = -MOVE_PLAYER_SPEED  # Устанавливаем начальную скорость
        elif keys[pygame.K_s]:
            self.y_speed = MOVE_PLAYER_SPEED
        else:
            # Если клавиша не нажата, замедляем движение
            self.y_speed *= 0.9  # Коэффициент замедления (чем меньше, тем плавнее остановка)

        if keys[pygame.K_a]:
            self.x_speed = -MOVE_PLAYER_SPEED
        elif keys[pygame.K_d]:
            self.x_speed = MOVE_PLAYER_SPEED
        else:
            self.x_speed *= 0.9  # Замедление по оси X

        # Обновляем позиции
        self.x += self.x_speed
        self.y += self.y_speed

        # Останавливаем игрока, если скорость становится очень маленькой
        if abs(self.x_speed) < 0.1:
            self.x_speed = 0
        if abs(self.y_speed) < 0.1:
            self.y_speed = 0