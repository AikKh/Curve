import pygame, sys
from settings import *
from time import time
from random import randrange
from svg import SVG
from curve import Curve
from vector import Vec2
from button import Button
from generator import Generator


pygame.init()

class Screen:

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Curve")
    
    clock = pygame.time.Clock()
    fps = 15
    
    def __init__(self):
        self._showing = False

        def next(): self.reset(); self.screen.fill(BLACK); self.draw_all(); pygame.display.flip()
        def show(): self._showing = not self._showing; self.screen.fill(BLACK); self.draw_all(); pygame.display.flip()
        def save(): svg = SVG(f"Example-{str(int(time()))[5:]}", WIDTH, HEIGHT); svg._params.clear(); \
                                                                                 svg.append(self._curve); \
                                                                                 svg.save()

        x = WIDTH // 20
        y = HEIGHT - HEIGHT // 15

        self._buttons = [
            Button(Vec2(x, y), Vec2(100, 50), "Next", next, (255, 165, 0)),
            Button(Vec2(x + 100, y), Vec2(100, 50), "Show", show, (0, 100, 100)),
            Button(Vec2(x + 200, y), Vec2(100, 50), "Save", save, (252, 243, 166)),
        ]

        self.reset()

    def reset(self):
        lines = Generator.joined_lines(randrange(3, 40))
        self._curve = Curve(lines)
        
    def draw_all(self):
        if self._showing:
            self._curve.draw_mains(self.screen)
            
        self._curve.draw(self.screen)

        for button in self._buttons:
            button.draw(self.screen)

    def handle_buttons(self, event: pygame.event.Event):
        for button in self._buttons:
            button.handle_event(event)


    def main(self):
        self.draw_all()
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                self.handle_buttons(event)

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.show_mains = not self.show_mains 
                        self.draw_all()
                        pygame.display.flip()
                        

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        svg = SVG(f"Example-{str(int(time()))[5:]}", WIDTH, HEIGHT)
                        
                        

                    

if __name__ == '__main__': 
    screen = Screen()
    screen.main()