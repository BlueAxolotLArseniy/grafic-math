from abc import ABC, abstractmethod
from pygame import Surface


class Screen(ABC):

    @abstractmethod
    def update(self, event): pass

    @abstractmethod
    def draw(self, sc: Surface): pass
