import pygame
from constants import SCREEN_SIZE, TITLE
from main_driver import MainDriver

class GameDriver:
    def __init__(self):
        # TODO: Start in init state
        self.state = "main"
        self.events = []
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.main_driver = MainDriver()

    def add_event(self, ev) -> None:
        self.events.append(ev)
        if self.state == "main":
            self.main_driver.add_event(ev)

    def clear_events(self) -> None:
        self.events.clear()
        self.main_driver.clear_events()

    def tick(self):
        if self.state == "main":
            self.main_driver.tick()
