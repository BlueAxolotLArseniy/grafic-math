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
                
                self.font = pygame.font.Font('fonts/Monocraft.otf', round(24))  # Use `round` for exact size
                
                self.text_fps = self.font.render(f'FPS {consts.FPS}', False, consts.WHITE)
                self.text_fps_rect = self.text_fps.get_rect(topleft=(20, 20))
                
                self.text_hp = self.font.render(f'HP {self.player.health}', False, consts.WHITE)
                self.text_hp_rect = self.text_hp.get_rect(bottomleft=(20, consts.SCREEN_HEIGHT-30-20))
                
                self.text_coords = self.font.render(f'COORDS X Y {int(self.camera.centerx//5)} {int(self.camera.centery//5)}',
                                                    False, consts.WHITE)
                self.text_coords_rect = self.text_coords.get_rect(topleft=(20, 50))

    def draw(self):
        self.player.draw(self.sc)

        if consts.ENABLE_ENEMIES:
            for enemy in self.enemies:
                enemy.draw(self.sc)

        for cave in self.caves:
            cave.draw(self.sc)

        if self.game_state.active_screen:
            self.game_state.active_screen.draw(self.sc)
        
        if self.game_state.debug_mode:
            self.sc.blit(self.text_fps, self.text_fps_rect)
            self.sc.blit(self.text_hp, self.text_hp_rect)
            self.sc.blit(self.text_coords, self.text_coords_rect)