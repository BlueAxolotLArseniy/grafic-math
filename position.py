from random import randint
from pygame import Rect


class Position(tuple):
    def __new__(cls, x: float, y: float):
        return super().__new__(cls, (x, y))

    @classmethod
    def from_tuple(cls, tup):
        """Creates a Position instance from a tuple (x, y)."""
        if isinstance(tup, tuple) and len(tup) == 2:
            return cls(*tup)
        raise ValueError("Tuple must have exactly two elements")

    @classmethod
    def random(cls, rect: Rect):
        return Position(
            randint(rect.left, rect.width),
            randint(rect.top, rect.height)
        )

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __add__(self, other):
        """Adds two Position objects."""
        if isinstance(other, Position):
            return Position(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __sub__(self, other):
        """Subtracts two Position objects."""
        if isinstance(other, Position):
            return Position(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, scalar: float):
        """Multiplies Position by a scalar."""
        if isinstance(scalar, (int, float)):
            return Position(self.x * scalar, self.y * scalar)
        return NotImplemented

    def __truediv__(self, scalar: float):
        """Divides Position by a scalar."""
        if isinstance(scalar, (int, float)) and scalar != 0:
            return Position(self.x / scalar, self.y / scalar)
        raise ValueError("Division by zero is not allowed")

    def __repr__(self):
        return f"x={self.x:.0f}, y={self.y:.0f}"