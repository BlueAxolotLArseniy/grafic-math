import pygame
import consts


class Map():
    def __init__(self, objs: tuple):
        self.objs = objs

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.last_key = event.key

        for obj in self.objs:

            if keys[pygame.K_s]:
                obj.y_speed = -consts.MOVE_PLAYER_SPEED
            elif keys[pygame.K_w]:
                obj.y_speed = consts.MOVE_PLAYER_SPEED
            else:
                # Если клавиша не нажата, замедляем движение
                obj.y_speed *= 0.9  # Коэффициент замедления (чем меньше, тем плавнее остановка)

            if keys[pygame.K_d]:
                obj.x_speed = -consts.MOVE_PLAYER_SPEED
            elif keys[pygame.K_a]:
                obj.x_speed = consts.MOVE_PLAYER_SPEED
            else:
                obj.x_speed *= 0.9  # Замедление по оси X

            obj.rect.centerx = int(obj.rect.centerx + obj.x_speed)
            obj.rect.centery = int(obj.rect.centery + obj.y_speed)

            # Останавливаем игрока, если скорость становится очень маленькой
            if abs(obj.x_speed) < 0.1:
                obj.x_speed = 0
            if abs(obj.y_speed) < 0.1:
                obj.y_speed = 0
