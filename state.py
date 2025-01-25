from ui.pause_screen import PauseScreen
from ui.screen import Screen


class GameState:

    debug_mode = True
    # todo: make it readonly property
    is_paused = False
    active_screen: Screen | None = None

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
