import pygame

from player import Player
from consts import FPS, SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from cave import Cave
from state import GameState
from game import Game

from camera import Camera

pygame.init()

game_state = GameState()

camera = Camera()

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, game_state, camera)
enemy = Enemy(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, player, 'WithOneBarrel', game_state)
enemy2 = Enemy(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, player, 'WithTwoBarrels', game_state)
cave = Cave(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, game_state)

clock = pygame.time.Clock()

game_operations = Game(sc,
                       player,
                       [enemy, enemy2],
                       [cave],
                       camera,
                       game_state
                       )

while 1:
    for event in pygame.event.get():
        game_operations.events(event)

    game_operations.update(event)
    game_operations.draw()

    clock.tick(FPS)
    pygame.display.update()
