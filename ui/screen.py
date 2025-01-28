from abc import ABC, abstractmethod
from pygame import Surface
from ui.blur import Blur


class ScreenABC(ABC):

    def __init__(self):
        self.blur = Blur()

    @abstractmethod
    def update(self, event): pass

    @abstractmethod
    def draw(self, sc: Surface):
        self.blur.draw(sc)
