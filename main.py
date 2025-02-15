import pygame
from bullets import Bullets
from enemy_type import EnemyType
from player import Player
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from cave import Cave
from state import GameState
from game import Game

pygame.init()

game_state = GameState()

bullets = Bullets()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, game_state, bullets)
enemy = Enemy(0, 0, player, EnemyType.single_cannon, game_state, bullets)
enemy2 = Enemy(SCREEN_WIDTH, SCREEN_HEIGHT, player, EnemyType.double_cannon, game_state, bullets)
cave = Cave(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, game_state)


game = Game(
    sc=sc,
    player=player,
    enemies=[enemy, enemy2],
    caves=[cave],
    game_state=game_state,
    bullets=bullets
)

game.run()
