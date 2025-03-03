from typing import List
import pygame
from bullets import Bullets
from enemies_spawner import EnemiesSpawner
from player import Player
from consts import ENEMY1_SETTINGS, ENEMY2_SETTINGS, GAME_FIELD_RECT, SCREEN_HEIGHT, SCREEN_WIDTH, STARS_COUNT
from enemy import Enemy
from cave import Cave
from position import Position
from game_state import GameState
from game import Game
from stars import Stars

pygame.init()

sc = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

game_state = GameState()

stars = Stars.random(STARS_COUNT, GAME_FIELD_RECT)
bullets = Bullets(game_state)
player = Player(Position(0, 0), game_state, bullets)
cave = Cave(0, 0, game_state, player)
enemies: List[Enemy] = []
enemies_spawner = EnemiesSpawner(game_state, enemies, player, bullets)

game = Game(
    sc=sc,
    player=player,
    enemies=enemies,
    caves=[cave],
    game_state=game_state,
    bullets=bullets,
    stars=stars,
    enemies_spawner=enemies_spawner
)

game.run()
