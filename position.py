class Position(tuple):
    def __new__(cls, x: float, y: float):
        return super().__new__(cls, (x, y))

    @classmethod
    def from_tuple(cls, tup):
        """Creates a Position instance from a tuple (x, y)."""
        if isinstance(tup, tuple) and len(tup) == 2:
            return cls(*tup)
        raise ValueError("Tuple must have exactly two elements")

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

    def __repr__(self):
        return f"x={self.x:.0f}, y={self.y:.0f}"
