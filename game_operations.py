import player
import consts
import pygame


class Game:
    def __init__(self, sc, player: player.Player, enemies: list, caves: list, camera, game_state):
        self.sc = sc
        self.player = player
        self.enemies = enemies
        self.caves = caves
        self.camera = camera
        self.game_state = game_state

    def events(self, event):
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                self.game_state.toggle_pause()

    def update(self, event):
        self.sc.fill((0, 0, 0))

        if self.game_state.active_screen:
            self.game_state.active_screen.update(event)

        if not self.game_state.is_paused:
            self.camera.update()
            self.player.update(self.camera.kx, self.camera.ky)
            for cave in self.caves:
                cave.update(self.camera.kx, self.camera.ky)

            if consts.ENABLE_ENEMIES:
                for enemy in self.enemies:
                    enemy.update(self.camera.kx, self.camera.ky)

            if self.game_state.debug_mode:
                print('Debug --> Player time(ticks): ' + str(self.player.time))
                print('Debug --> Number of bullets: ' + str(len(self.player.bullets)))
                print('Debug --> FPS: ' + str(consts.FPS))

    def draw(self):
        self.player.draw(self.sc)

        if consts.ENABLE_ENEMIES:
            for enemy in self.enemies:
                enemy.draw(self.sc)

        for cave in self.caves:
            cave.draw(self.sc)

        if self.game_state.active_screen:
            self.game_state.active_screen.draw(self.sc)
