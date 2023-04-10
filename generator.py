from random import randrange
from settings import *
from line import Line


class Generator:

    @staticmethod
    def get_color(n: int, max: int):
        t = int((n / max) * 255)
        return (t, 0, 255 - t)

    @staticmethod
    def random_lines(amount):
        return [Line(randrange(WIDTH), randrange(HEIGHT), randrange(WIDTH), randrange(HEIGHT), 
        Generator.get_color(i, amount)) for i in range(amount + 1)]
         
    @staticmethod
    def joined_lines(amount):
        lines = []
        points = [(randrange(WIDTH), randrange(HEIGHT)) for _ in range(amount + 1)]
        
        for i in range(amount):
            x1, y1 = points[i]
            x2, y2 = points[i + 1]
            lines.append(Line(x1, y1, x2, y2, Generator.get_color(i, amount)))
        
        return lines
        
    