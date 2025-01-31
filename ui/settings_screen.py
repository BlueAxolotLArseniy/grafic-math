from typing import TYPE_CHECKING
from ui.button import Button
from ui.screen import ScreenABC

if TYPE_CHECKING:
    from state import GameState


class SettingsScreen(ScreenABC):

    def __init__(self, parent_screen: ScreenABC, game_state: 'GameState'):
        super().__init__()
        self.game_state = game_state
        self.parent_screen = parent_screen

        self.add_button(Button(0.8, 'Режим Отладки', action=self.toggle_debug_mode))
        self.add_button(Button(0.8, 'Назад', action=self.back))

    def toggle_debug_mode(self):
        self.game_state.debug_mode = not self.game_state.debug_mode

    def back(self):
        self.game_state.active_screen = self.parent_screen
