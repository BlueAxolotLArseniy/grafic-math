import pygame
import consts

class Camera():
    def __init__(self):
        self.kx = 0
        self.ky = 0
    
    def update(self):
        keys = pygame.key.get_pressed()
                
        if keys[pygame.K_s]:
            self.ky = -consts.MOVE_PLAYER_SPEED
        elif keys[pygame.K_w]:
            self.ky = consts.MOVE_PLAYER_SPEED
        else:
            # Если клавиша не нажата, замедляем движение
            self.ky *= 0.9  # Коэффициент замедления (чем меньше, тем плавнее остановка)

        if keys[pygame.K_d]:
            self.kx = -consts.MOVE_PLAYER_SPEED
        elif keys[pygame.K_a]:
            self.kx = consts.MOVE_PLAYER_SPEED
        else:
            self.kx *= 0.9  # Замедление по оси X

        # Останавливаем игрока, если скорость становится очень маленькой
        if abs(self.kx) < 0.1:
            self.kx = 0
        if abs(self.ky) < 0.1:
            self.ky = 0