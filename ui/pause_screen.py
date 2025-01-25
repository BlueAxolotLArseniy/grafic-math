from pygame import Surface
import pygame
from button import Button
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from state import GameState


class PauseScreen():

    def __init__(self, game_state: GameState):

        self.game_state = game_state

        self.blur_sc = pygame.surface.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))

        self.exit_button = Button(0.8, (SCREEN_WIDTH/2, (SCREEN_HEIGHT/3)*2), 'Выйти')
        self.settings_button = Button(0.8, (SCREEN_WIDTH/2, (SCREEN_HEIGHT/3)*1.5), 'Настройки')
        self.continue_button = Button(0.8, (SCREEN_WIDTH/2, SCREEN_HEIGHT/3), 'Продолжить')
        self.debug_button = Button(0.8, (SCREEN_WIDTH/2, (SCREEN_HEIGHT/3)*1.5), 'Режим Отладки')

    def update(self, event):

        mouse_pos = pygame.mouse.get_pos()

        if self.game_state.is_paused:
            if event.type == pygame.MOUSEBUTTONUP:
                # if self.game_state.debug_mode:
                # print(f"Mouse clicked at position: {mouse_pos}")
                # print(f"Exit button rect: {self.exit_button.image_rect}")
                # print(f"Continue button rect: {self.continue_button.image_rect}")
                # print(f"Settings button rect: {self.settings_button.image_rect}")
                # print(f"Debug button rect: {self.debug_button.image_rect}")
                if not self.game_state.settings_button_clicked:
                    if self.exit_button.image_rect.collidepoint(mouse_pos):
                        exit()
                    if self.continue_button.image_rect.collidepoint(mouse_pos):
                        self.game_state.is_paused = False
                    if self.settings_button.image_rect.collidepoint(mouse_pos):
                        self.game_state.settings_button_clicked = True
                else:
                    if self.debug_button.image_rect.collidepoint(mouse_pos):
                        self.game_state.debug_mode = not self.game_state.debug_mode
                        self.game_state.settings_button_clicked = False

    def draw(self, sc: Surface,):
        if self.game_state.is_paused:
            self.blur_sc.fill((0, 0, 0))
            self.blur_sc.set_alpha(200)
            sc.blit(self.blur_sc, (0, 0))

            if self.game_state.settings_button_clicked:
                # self.debug_button.update()
                self.debug_button.draw(sc)
            else:
                # self.exit_button.update()
                # self.continue_button.update()
                # self.settings_button.update()

                self.exit_button.draw(sc)
                self.continue_button.draw(sc)
                self.settings_button.draw(sc)
