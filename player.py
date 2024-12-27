import pygame
import random
import math
from bullet import Bullet
from common import radians_to_degrees
from consts import BULLET_SPEED, MOVE_PLAYER_SPEED
pygame.init()


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, filename):
        self.x = x
        self.y = y
        self.real_time = 0
        self.image = pygame.image.load(filename).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))  # a
        self.rect = self.image.get_rect(center=(x, y))
        self.original_image = self.image
        self.original_rect = self.rect.copy()
        self.x_speed = 0
        self.y_speed = 0
        self.__angle = 0
        self.bullets: list[Bullet] = []

    def _rotate(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        rel_x, rel_y = mouse_x - self.x, mouse_y - self.y
        self.__angle = math.atan2(rel_y, rel_x)
        self.image = pygame.transform.rotate(self.original_image, int(radians_to_degrees(-self.__angle)))
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

        self._rotate()

        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if left:
            bullet = Bullet(self.__angle, BULLET_SPEED, self.x, self.y)
            self.bullets.append(bullet)

        for bullet in self.bullets:
            bullet.update()

    def draw(self, sc: pygame.Surface):
        sc.blit(self.image, self.rect)

        for bullet in self.bullets:
            bullet.draw(sc)
