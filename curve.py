import pygame
from settings import *
from line import Line
from vector import Vec2


class Curve:

    def __init__(self, lines: list[Line]):
        self._main_lines = lines
        self._points = self.get_curve_points(self._main_lines, 150)


    def get_curve_points(self, main_lines: list[Line], density: int) -> list[Vec2]:
        return [
            self.point(main_lines, (1 / density) * i)
            for i in range(density + 1)
        ]


    def point(self, lines: list[Line], k: float) -> Vec2:
        if len(lines) == 1:
            return Curve.point_on_line(lines[0], k)

        points = [
            Curve.point_on_line(lines[i], k)
            for i in range(len(lines))
        ]

        return self.point(Curve.lines_between_pointes(points), k)


    def point_on_line(line: Line, k: float) -> Vec2:
        # 0 < k < 1
        d = line.dir() * k
        return line._p1 + d

    def lines_between_pointes(points: list[Vec2]):
        lines = []
        
        for i in range(len(points) - 1):
            x1, y1 = points[i].to_tuple()
            x2, y2 = points[i + 1].to_tuple()
            lines.append(Line(x1, y1, x2, y2))
        
        return lines

    def draw(self, screen: pygame.Surface):
        for i in range(len(self._points) - 1):
            p1 = self._points[i].to_tuple()
            p2 = self._points[i + 1].to_tuple()

            pygame.draw.line(screen, GREEN, p1, p2, 3)

    def draw_mains(self, screen: pygame.Surface):
        for l in self._main_lines:
            pygame.draw.line(screen, l._color, l._p1.to_tuple(), l._p2.to_tuple(), 3)

    def __str__(self):
        points = self.get_curve_points(self._main_lines, 1000)
        s = '<path d = "%s" stroke="black" fill="transparent"/>'

        m = "%s %s" % (points[0].to_tuple())
        c = "%s %s" % (points[1].to_tuple())

        path = f"M {m} C {c}, "

        for i in range(2, len(points)):
            p = "%s %s" % (points[i].to_tuple())
            path += p; path += ", "

        return s % path