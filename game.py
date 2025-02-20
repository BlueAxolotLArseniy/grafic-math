# from camera import Camera
from bullets import Bullets
from cave import Cave
from common import draw_text
import consts
import pygame
from pygame.event import Event
from typing import TYPE_CHECKING, List

from enemies_spawner import EnemiesSpawner
from enemy import Enemy
from player import Player
from player_state import PlayerState
from position import Position
from stars import Stars

if TYPE_CHECKING:
    from game_state import GameState


class Game:
    def __init__(
        self,
        sc,
        player: Player,
        enemies: List[Enemy],
        caves: List[Cave],
        game_state: 'GameState',
        bullets: Bullets,
        stars: Stars,
        enemies_spawner: EnemiesSpawner
    ):
        self.sc = sc
        self.player = player
        self.enemies = enemies
        self.caves = caves
        self.bullets = bullets
        self.__stars = stars
        self.game_state = game_state
        self.enemies_spawner = enemies_spawner
        self.font = pygame.font.Font('fonts/Monocraft.otf', round(24))  # Use `round` for exact size

    def __keyboard_events(self, events: List[Event]):

        for event in events:
            if event.type == pygame.QUIT:
                exit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.game_state.toggle_pause()

                if event.key == pygame.K_F3:
                    self.game_state.debug_mode = not self.game_state.debug_mode

    def update(self):

        events: List[Event] = pygame.event.get()

        self.__keyboard_events(events)

        self.__respawn()
        if self.game_state.active_screen:
            self.game_state.active_screen.update(events)

        if self.game_state.is_paused:
            return

        self.enemies_spawner.update()
        self.bullets.update()
        self.player.update()
        for cave in self.caves:
            cave.update()

        if consts.ENABLE_ENEMIES:
            for enemy in self.enemies:
                enemy.update()

        if self.game_state.debug_mode:
            print(f'Debug --> Player time(ticks): {self.player.time}')
            print(f'Debug --> Number of bullets: {self.bullets.count()}')

    def __respawn(self):
        if self.game_state.player_state == PlayerState.respawn:
            self.game_state.player_state = PlayerState.active
            self.game_state.unpause()
            self.player.respawn()
            for enemy in self.enemies:
                enemy.respawn()

    def draw(self, clock: pygame.time.Clock):
        self.sc.fill((0, 0, 0))

        self.__stars.draw(self.sc, self.player)

        self.player.draw(self.sc)

        self.bullets.draw(self.sc, self.player)

        if consts.ENABLE_ENEMIES:
            for enemy in self.enemies:
                enemy.draw(self.sc, self.player)

        for cave in self.caves:
            cave.draw(self.sc, self.player)

        if self.game_state.active_screen:
            self.game_state.active_screen.draw(self.sc)

        if self.game_state.debug_mode:

            draw_text(self.sc, f'FPS {int(clock.get_fps())}', Position(20, 20), consts.WHITE, self.font)

    def run(self):
        clock = pygame.time.Clock()
        while 1:
            self.update()
            self.draw(clock)
            clock.tick(consts.FPS)
            pygame.display.update()
