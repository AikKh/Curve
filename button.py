import pygame
from vector import Vec2


class Button:
    def __init__(self, center_pos: Vec2, size: Vec2, text: str, func, color=(255, 255, 255)):
        self._func = func
        self._rect = pygame.Rect(int(center_pos._x - size._y / 2), int(center_pos._y - size._y / 2), size._x, size._y)
        self._label = pygame.font.Font(None, 24).render(text, True, (0, 0, 0))
        self._color = color

    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self._color, self._rect)
        label_rect = self._label.get_rect(center=self._rect.center)
        screen.blit(self._label, label_rect)
        
    def handle_event(self, event: pygame.event.Event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self._rect.collidepoint(event.pos):
                self._func()
