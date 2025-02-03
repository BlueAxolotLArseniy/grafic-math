from abc import ABC
from pygame import Surface
from consts import SCREEN_HEIGHT, SCREEN_WIDTH
from ui.blur import Blur
from ui.button import Button


class ScreenABC(ABC):

    def __init__(self):
        self.blur = Blur()
        self.buttons: list[Button] = []

    def add_button(self, button: Button):
        self.buttons.append(button)
        self.update_button_positions()

    def update_button_positions(self):
        buttons_count = len(self.buttons)
        for button_num in range(0, buttons_count):
            button_pos = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/buttons_count/2) + (SCREEN_HEIGHT/buttons_count*button_num))
            self.buttons[button_num].set_position(button_pos)

    def update(self, event):
        for button in self.buttons:
            button.update(event)

    def draw(self, sc: Surface):
        self.blur.draw(sc)
        for button in self.buttons:
            button.draw(sc)
