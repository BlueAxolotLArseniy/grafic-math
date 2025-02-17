
from random import randint


class Color(tuple):
    def __new__(cls, r: int, g: int, b: int):
        return super().__new__(cls, (r, g, b))

    @classmethod
    def random(cls, r_min: int, r_max: int, g_min: int, g_max: int, b_min: int, b_max: int) -> 'Color':
        return Color(
            randint(r_min, r_max),
            randint(g_min, g_max),
            randint(b_min, b_max)
        )
