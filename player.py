import pygame

from bullet import Bullet
from common import get_angle_to_mouse, rotate_image
from consts import BASE_HEALTH, SCREEN_WIDTH, SCREEN_HEIGHT
from state import GameState


class Player():
    def __init__(self, x, y, game_state: GameState):
        self.image = pygame.image.load('images/game_textures/ship.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*10, self.image.get_height()*10))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(x, y))
        self.original_rect = self.rect.copy()

        self.time = 0

        self.bullets: list[Bullet] = []

        self.health = BASE_HEALTH

        self.game_state = game_state

    def _rotate(self):
        self.angle = get_angle_to_mouse(self.rect.centerx, self.rect.centery)
        self.image, self.rect = rotate_image(self.original_image, self.rect.center, self.angle)

    def update(self, kx, ky):
        self.time += 1
        self._rotate()

        left, middle, right = pygame.mouse.get_pressed()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if self.time % 4 == 0:
            if left:
                bullet = Bullet(self.angle, self.rect.center, False, 1, self.game_state)
                self.bullets.append(bullet)

        for b in range(len(self.bullets)-1):
            if self.bullets[b].rect.centerx > SCREEN_WIDTH + self.bullets[b].rect.width or self.bullets[b].rect.centerx < 0 - self.bullets[b].rect.width:
                self.bullets.pop(b)
                break
            if self.bullets[b].rect.centery > SCREEN_HEIGHT + self.bullets[b].rect.height or self.bullets[b].rect.centery < 0 - self.bullets[b].rect.height:
                self.bullets.pop(b)
                break

        for bullet in self.bullets:
            bullet.update(kx, ky)

        for b in self.bullets:
            if self.rect.colliderect(b.rect) and b.affiliation != False:
                self.health -= 1 * b.koefficient

    def draw_hp(self, sc):
        pygame.draw.rect(sc, (255, 255, 255), (19, 459, 202, 22), 1)
        pygame.draw.rect(sc, (0, 255, 0), (20, 460, self.health*2, 20))

    def draw(self, sc: pygame.Surface):
        for bullet in self.bullets:
            bullet.draw(sc)

        sc.blit(self.image, self.rect)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, (255, 255, 255), self.rect, 2)

        self.draw_hp(sc)
