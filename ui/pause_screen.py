from typing import TYPE_CHECKING
from pygame import Surface
from ui.button import Button
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from ui.screen import Screen
from ui.settings_screen import SettingsScreen

if TYPE_CHECKING:
    from state import GameState


class PauseScreen(Screen):

    def __init__(self, game_state: 'GameState'):
        super().__init__()
        self.game_state = game_state
        self.exit_button = Button(0.8, (SCREEN_WIDTH/2, (SCREEN_HEIGHT/3)*2), 'Выйти')
        self.settings_button = Button(0.8, (SCREEN_WIDTH/2, (SCREEN_HEIGHT/3)*1.5), 'Настройки')
        self.continue_button = Button(0.8, (SCREEN_WIDTH/2, SCREEN_HEIGHT/3), 'Продолжить')

    def update(self, event):

        if self.exit_button.is_clicked(event):
            exit()

        if self.continue_button.is_clicked(event):
            self.game_state.unpause()

        if self.settings_button.is_clicked(event):
            self.game_state.active_screen = SettingsScreen(self, self.game_state)

    def draw(self, sc: Surface):
        super().draw(sc)
        self.exit_button.draw(sc)
        self.continue_button.draw(sc)
        self.settings_button.draw(sc)
