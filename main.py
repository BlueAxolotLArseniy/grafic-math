import pygame
from enemy_type import EnemyType
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
enemy = Enemy(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, player, EnemyType.single_cannon, game_state)
enemy2 = Enemy(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, player, EnemyType.double_cannon, game_state)
cave = Cave(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, game_state)

clock = pygame.time.Clock()

game = Game(
    sc=sc,
    player=player,
    enemies=[enemy, enemy2],
    caves=[cave],
    camera=camera,
    game_state=game_state
)

while 1:
    game.update()
    game.draw()

    clock.tick(FPS)
    pygame.display.update()
