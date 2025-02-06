import pygame

from bullet import Bullet
from common import get_angle_to_mouse, rotate_image
from consts import BASE_PLAYER_HEALTH, GREEN, SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE, ORANGE, YELLOW, RED
from state import GameState


class Player():
    def __init__(self, x, y, game_state: GameState):
        self.image = pygame.image.load('images/game_textures/ship.png').convert()
        self.image.set_colorkey(BLACK)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*5, self.image.get_height()*5))
        self.original_image = self.image

        self.rect = self.image.get_rect(center=(x, y))
        self.original_rect = self.rect.copy()

        self.time = 0

        self.bullets: list[Bullet] = []

        self.health = BASE_PLAYER_HEALTH

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
                bullet = Bullet(self.angle, self.rect.center, 'not attacks a player', 1, self.game_state)
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
            if self.rect.colliderect(b.rect) and b.attack_affiliation == 'attacks a player':
                self.health -= 1 * b.koefficient

    def draw_hp(self, sc):
        pygame.draw.rect(sc, WHITE, (19, SCREEN_HEIGHT-19-22, 202, 22), 1)
        if self.health >= 75:
            pygame.draw.rect(sc, GREEN, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))
        elif self.health >= 50:
            pygame.draw.rect(sc, YELLOW, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))
        elif self.health >= 25:
            pygame.draw.rect(sc, ORANGE, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))
        elif self.health >= 0:
            pygame.draw.rect(sc, RED, (20, SCREEN_HEIGHT-20-20, self.health*2, 20))

    def draw(self, sc: pygame.Surface):
        for bullet in self.bullets:
            bullet.draw(sc)

        sc.blit(self.image, self.rect)

        if self.game_state.debug_mode:
            pygame.draw.rect(sc, WHITE, self.rect, 2)

        self.draw_hp(sc)
