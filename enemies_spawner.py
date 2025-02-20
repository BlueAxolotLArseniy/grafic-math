

import random
from typing import List

import pygame

from bullets import Bullets
from consts import ENEMY1_SETTINGS, ENEMY2_SETTINGS
from enemy import Enemy
from game_state import GameState
from player import Player
from position import Position


class EnemiesSpawner:

    def __init__(self, game_state: GameState, enemies: List[Enemy], player: Player, bullets: Bullets):
        self.__enemies = enemies
        self.__game_state = game_state
        self.__next_spawn_ticks = 0
        self.__player = player
        self.__bullets = bullets

    def update(self):

        ticks = pygame.time.get_ticks()

        if ticks < self.__next_spawn_ticks:
            return

        enemy = self.__get_random_enemy()
        self.__enemies.append(enemy)

        self.__next_spawn_ticks = ticks + 60 * 50

    def __get_random_enemy(self) -> Enemy:
        random_num = random.randint(1, 2)

        if random_num == 1:
            return Enemy(Position(-400, -275), self.__player, ENEMY1_SETTINGS, self.__game_state, self.__bullets)
        else:
            return Enemy(Position(400, 275), self.__player, ENEMY2_SETTINGS, self.__game_state, self.__bullets)
