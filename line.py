import math
import pygame
from vector import Vec2


class Line:

    def __init__(self, x1: int, y1: int, x2: int, y2: int, color: tuple[int] = (0, 0, 255)):
        self._p1 = Vec2(x1, y1)
        self._p2 = Vec2(x2, y2)

        self._color = color

    def dir(self):
        x = self._p2._x - self._p1._x
        y = self._p2._y - self._p1._y

        return Vec2(x, y)

    def distance(self):
        return math.sqrt((self._p1._x - self._p2._x)**2 + (self._p1._y - self._p2._y)**2)

    def draw(self, screen: pygame.Surface):
        pygame.draw.line(screen, self._color, self._p1.to_tuple(), self._p2.to_tuple(), 3)
