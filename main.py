import pygame
from bullets import Bullets
from player import Player
from consts import ENEMY1_SETTINGS, ENEMY2_SETTINGS, SCREEN_HEIGHT, SCREEN_WIDTH
from enemy import Enemy
from cave import Cave
from position import Position
from game_state import GameState
from game import Game

pygame.init()
sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

game_state = GameState()
bullets = Bullets(game_state)
player = Player(Position(0, 0), game_state, bullets)
enemy = Enemy(Position(-400, -275), player, ENEMY1_SETTINGS, game_state, bullets)
enemy2 = Enemy(Position(400, 275), player, ENEMY2_SETTINGS, game_state, bullets)
cave = Cave(0, 0, game_state)

game = Game(
    sc=sc,
    player=player,
    enemies=[enemy, enemy2],
    caves=[cave],
    game_state=game_state,
    bullets=bullets
)

game.run()
