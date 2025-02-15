# from camera import Camera
from bullets import Bullets
from cave import Cave
import player
import consts
import pygame
from pygame.event import Event
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from state import GameState


class Game:
    def __init__(
        self,
        sc,
        player: player.Player,
        enemies: list,
        caves: List[Cave],
        game_state: 'GameState',
        bullets: Bullets
    ):
        self.sc = sc
        self.player = player
        self.enemies = enemies
        self.caves = caves
        self.bullets = bullets
        self.game_state = game_state
        self.font = pygame.font.Font('fonts/Monocraft.otf', round(24))  # Use `round` for exact size

    def __events(self, events: List[Event]):

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

        self.__events(events)
        # self.__respawn()

        self.bullets.update()

        if self.game_state.active_screen:
            self.game_state.active_screen.update(events)

        if not self.game_state.is_paused:
            self.player.update()
            for cave in self.caves:
                cave.update()

            if consts.ENABLE_ENEMIES:
                for enemy in self.enemies:
                    enemy.update()

            if self.game_state.debug_mode:
                print(f'Debug --> Player time(ticks): {self.player.time}')
                print(f'Debug --> Number of bullets: {self.bullets.count()}')

            self.text_fps = self.font.render(f'FPS {consts.FPS}', False, consts.WHITE)
            self.text_fps_rect = self.text_fps.get_rect(topleft=(20, 20))

            self.text_hp = self.font.render(f'HP {self.player.health}', False, consts.WHITE)
            self.text_hp_rect = self.text_hp.get_rect(bottomleft=(20, consts.SCREEN_HEIGHT-30-20))

            # self.text_coords = self.font.render(f'COORDS X Y {int(self.camera.centerx)} {int(self.camera.centery)}', False, consts.WHITE)
            # self.text_coords_rect = self.text_coords.get_rect(topleft=(20, 50))

    # def __respawn(self):
    #     if self.game_state.player_state == PlayerState.respawn:
    #         self.game_state.unpause()

    #         print('RESPAWN')

    #         self.player.health = 100

    #         self.camera.kx = self.camera.centerx - self.center_rect.centerx
    #         self.camera.ky = self.camera.centery - self.center_rect.centery

    #         self.game_state.player_state = PlayerState.active

    def draw(self):
        self.sc.fill((0, 0, 0))

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
            self.sc.blit(self.text_fps, self.text_fps_rect)
            self.sc.blit(self.text_hp, self.text_hp_rect)
            # self.sc.blit(self.text_coords, self.text_coords_rect)

    def run(self):
        clock = pygame.time.Clock()
        while 1:
            self.update()
            self.draw()
            clock.tick(consts.FPS)
            pygame.display.update()
