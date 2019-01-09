import pygame
from constants import SCREEN_SIZE, TITLE

class GameDriver:
    def __init__(self):
        self.events = []
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)

    def add_event(self, ev):
        self.events.append(ev)

    def clear_events(self):
        self.events.clear()

