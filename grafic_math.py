import pygame
import random
import math
from player import Player
from contstants import FPS
pygame.init()

sc = pygame.display.set_mode((800, 500))

player = Player(400, 250, 'images/ship.png')

clock = pygame.time.Clock()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.rect.centerx -= 20

    sc.fill((0, 0, 0))
    player.rotate()
    sc.blit(player.image, player.rect)
    clock.tick(FPS)
    pygame.display.update()