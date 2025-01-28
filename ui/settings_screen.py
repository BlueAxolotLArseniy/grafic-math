from typing import TYPE_CHECKING
from pygame import Surface
from ui.button import Button
from consts import BUTTON_DOWN_POS, BUTTON_MIDDLE_POS
from ui.screen import ScreenABC

if TYPE_CHECKING:
    from state import GameState


class SettingsScreen(ScreenABC):

    def __init__(self, parent_screen: ScreenABC, game_state: 'GameState'):
        super().__init__()
        self.game_state = game_state
        self.parent_screen = parent_screen
        self.debug_button = Button(0.8, BUTTON_MIDDLE_POS, 'Режим Отладки')
        self.back_button = Button(0.8, BUTTON_DOWN_POS, 'Назад')

    def update(self, event):

        if self.debug_button.is_clicked(event):
            self.game_state.debug_mode = not self.game_state.debug_mode

        if self.back_button.is_clicked(event):
            self.game_state.active_screen = self.parent_screen

    def draw(self, sc: Surface):
        super().draw(sc)
        self.debug_button.draw(sc)
        self.back_button.draw(sc)
