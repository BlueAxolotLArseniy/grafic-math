import pygame
from bullet import Bullet
from common import get_angle_to_mouse, radians_to_degrees
from consts import BULLET_SPEED, MOVE_PLAYER_SPEED, BASE_PLAYER_HEALTH

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        self.image = pygame.image.load('images/ship.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image
        
        self.rect = self.image.get_rect(center=(x, y))
        self.original_rect = self.rect.copy()
        
        self.x_speed = 0
        self.y_speed = 0
        
        self.time = 0
        self.bullets: list[Bullet] = []
        
        self.health = BASE_PLAYER_HEALTH

    def _rotate(self):
        self.angle = get_angle_to_mouse(self.rect.centerx, self.rect.centery)
        self.image = pygame.transform.rotate(self.original_image, int(radians_to_degrees(-self.angle)))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

    def update(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                self.last_key = event.key

        self.time += 1
        
        if keys[pygame.K_w]:
            self.y_speed = -MOVE_PLAYER_SPEED
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

        self.rect.centerx = int(self.rect.centerx + self.x_speed)
        self.rect.centery = int(self.rect.centery + self.y_speed)

        # Останавливаем игрока, если скорость становится очень маленькой
        if abs(self.x_speed) < 0.1:
            self.x_speed = 0
        if abs(self.y_speed) < 0.1:
            self.y_speed = 0

        self._rotate()

        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.time % 2 == 0:
            if left:
                bullet = Bullet(self.angle, self.rect.center, False, 1)
                self.bullets.append(bullet)

        for bullet in self.bullets:
            bullet.update()

    def draw(self, sc: pygame.Surface):

        for bullet in self.bullets:
            bullet.draw(sc)

        sc.blit(self.image, self.rect)

        #--------------HP--------------
        pygame.draw.rect(sc, (255, 255, 255), (19, 459, 202, 22), 1)
        
        pygame.draw.rect(sc, (0, 255, 0), (20, 460, self.health*2, 20))
        
        for b in self.bullets:
            if self.rect.colliderect(b.rect):
                self.health -= 1 * b.koefficient
        #------------------------------
