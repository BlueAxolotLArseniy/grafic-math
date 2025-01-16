import pygame
from bullet import Bullet
from common import get_angle_to_mouse, radians_to_degrees, rotate_image
from consts import BASE_PLAYER_HEALTH, DEBUG_MODE


class Player():
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
        self.image, self.rect = rotate_image(self.original_image, self.rect.center, self.angle)

    def update(self):
        self.time += 1
        self._rotate()

        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.time % 2 == 0:
            if left:
                bullet = Bullet(self.angle, self.rect.center, False, 1)
                self.bullets.append(bullet)

        for b in range(len(self.bullets)-1):
            if self.bullets[b].rect.centerx > 800 + self.bullets[b].rect.width or self.bullets[b].rect.centerx < 0 - self.bullets[b].rect.width:
                self.bullets.pop(b)
                break
            if self.bullets[b].rect.centery > 500 + self.bullets[b].rect.height or self.bullets[b].rect.centery < 0 - self.bullets[b].rect.height:
                self.bullets.pop(b)
                break

        for bullet in self.bullets:
            bullet.update()

        for b in self.bullets:
            if self.rect.colliderect(b.rect) and b.affiliation != False:
                self.health -= 1 * b.koefficient

    def draw(self, sc: pygame.Surface):

        for bullet in self.bullets:
            bullet.draw(sc)

        sc.blit(self.image, self.rect)

        if DEBUG_MODE:
            pygame.draw.rect(sc, (255, 255, 255), self.rect, 2)

        # --------------HP--------------
        pygame.draw.rect(sc, (255, 255, 255), (19, 459, 202, 22), 1)
        pygame.draw.rect(sc, (0, 255, 0), (20, 460, self.health*2, 20))
        # ------------------------------
