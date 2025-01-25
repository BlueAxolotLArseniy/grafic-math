from pygame import Surface
import pygame
from button import Button
import consts
from state import GameState


class UI_Pause():

    def __init__(self, sc: Surface, game_state: GameState):

        self.game_state = game_state

        self.sc = sc
        self.blur_sc = pygame.surface.Surface((800, 500))

        self.exit_button = Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*2), 'Выйти')
        self.settings_button = Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*1.5), 'Настройки')
        self.continue_button = Button(0.8, (sc.get_width()/2, sc.get_height()/3), 'Продолжить')
        self.debug_button = Button(0.8, (sc.get_width()/2, (sc.get_height()/3)*1.5), 'Режим Отладки')

    def update(self, event):

        mouse_pos = pygame.mouse.get_pos()

        if self.game_state.pause_mode:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if consts.DEBUG_MODE:
                    print(f"Mouse clicked at position: {mouse_pos}")
                    print(f"Exit button rect: {self.exit_button.image_rect}")
                    print(f"Continue button rect: {self.continue_button.image_rect}")
                    print(f"Settings button rect: {self.settings_button.image_rect}")
                    print(f"Debug button rect: {self.debug_button.image_rect}")
                if not self.game_state.settings_button_clicked:
                    if self.exit_button.image_rect.collidepoint(mouse_pos):
                        exit()
                    if self.continue_button.image_rect.collidepoint(mouse_pos):
                        self.game_state.pause_mode = False
                    if self.settings_button.image_rect.collidepoint(mouse_pos):
                        self.game_state.settings_button_clicked = True
                else:
                    if self.debug_button.image_rect.collidepoint(mouse_pos):
                        print(consts.DEBUG_MODE)
                        consts.DEBUG_MODE = not consts.DEBUG_MODE
                        self.game_state.debug_mode = consts.DEBUG_MODE
                        print(consts.DEBUG_MODE)
                        self.game_state.settings_button_clicked = False

    def draw(self):
        if self.game_state.pause_mode:
            self.blur_sc.fill((0, 0, 0))
            self.blur_sc.set_alpha(200)
            self.sc.blit(self.blur_sc, (0, 0))

            if self.game_state.settings_button_clicked:
                self.debug_button.update()
                self.debug_button.draw(self.sc)
            else:
                self.exit_button.update()
                self.continue_button.update()
                self.settings_button.update()

                self.exit_button.draw(self.sc)
                self.continue_button.draw(self.sc)
                self.settings_button.draw(self.sc)
