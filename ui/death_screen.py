from typing import TYPE_CHECKING
from ui.button import Button
from ui.screen import ScreenABC

if TYPE_CHECKING:
    from state import GameState


class DeathScreen(ScreenABC):

    def __init__(self, player, camera):
        super().__init__()
        
        self.player = player
        self.camera = camera
        

        self.add_button(Button(1, 'Выйти из игры', action=lambda: exit()))
        self.add_button(Button(1, 'Возродиться', action=self.respawn))
        
    def respawn(self):
        self.player.health = 100
        self.camera.kx = -self.camera.centerx
        self.camera.ky = -self.camera.centery
        
        