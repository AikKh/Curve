import math

class Vec2:

    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __mul__(self, num: float):
        return Vec2(self._x * num, self._y * num)

    def __truediv__(self, num: float):
        return Vec2(self._x / num, self._y / num)

    def __add__(self, num: float):
        return Vec2(self._x + num, self._y + num)

    def __add__(self, vec):
        return Vec2(self._x + vec._x, self._y + vec._y)

    def __sub__(self, num: float):
        return Vec2(self._x - num, self._y - num)

    def __len__(self):
        return int(math.sqrt(self._x**2 + self._y**2))

    def __str__(self):
        return f"({self._x}, {self._y})"

    def to_tuple(self):
        return (self._x, self._y)
