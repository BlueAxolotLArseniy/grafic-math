from typing import TYPE_CHECKING
from ui.button import Button
from ui.screen import ScreenABC
from ui.settings_screen import SettingsScreen

if TYPE_CHECKING:
    from state import GameState


class PauseScreen(ScreenABC):

    def __init__(self, game_state: 'GameState'):
        super().__init__()
        self.game_state = game_state

        self.add_button(Button(1, 'Выйти', action=lambda: exit()))
        self.add_button(Button(1, 'Настройки', action=self.open_settings_screen))
        self.add_button(Button(1, 'Продолжить', action=lambda: self.game_state.unpause()))

    def open_settings_screen(self):
        self.game_state.active_screen = SettingsScreen(parent_screen=self, game_state=self.game_state)
