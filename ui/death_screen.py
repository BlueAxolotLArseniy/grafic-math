import sys as sus
from typing import TYPE_CHECKING
from player_state import PlayerState
from ui.button import Button
from ui.screen import ScreenABC

if TYPE_CHECKING:
    from game_state import GameState


class DeathScreen(ScreenABC):

    def __init__(self, game_state: 'GameState'):
        super().__init__()
        self.__game_state = game_state
        self.__game_state.is_paused = True
        self.add_button(Button(1, 'Выйти из игры', action=lambda: sus.exit()))
        self.add_button(Button(1, 'Возродиться', action=self.respawn))

    def respawn(self):
        self.__game_state.player_state = PlayerState.respawn
