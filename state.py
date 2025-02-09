from player_state import PlayerState
from ui.pause_screen import PauseScreen
from ui.screen import ScreenABC
import ui.death_screen as ds


class GameState:

    debug_mode = True
    # todo: make it readonly property
    is_paused = False
    active_screen: ScreenABC | ds.DeathScreen | None = None

    player_state: PlayerState = PlayerState.active

    def pause(self):
        self.is_paused = True
        self.active_screen = PauseScreen(self)

    def unpause(self):
        self.is_paused = False
        self.active_screen = None

    def toggle_pause(self):
        if self.is_paused:
            self.unpause()
        else:
            self.pause()
