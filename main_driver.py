import pygame
from constants import SCREEN_SIZE, TILE_SIZE
from player import Player
from xml_utils import load_xml, write_xml


class MainDriver:
    def __init__(self, screen):
        pygame.key.set_repeat(1, 1)
        self.screen = screen
        self.events = []
        self.grid_width = SCREEN_SIZE[0] // TILE_SIZE
        self.grid_height = SCREEN_SIZE[1] // TILE_SIZE
        self.grid = [
            [
                None for _ in range(self.grid_width)
            ]
            for _ in range(self.grid_height)
        ]
        self.objects = [
            Player(self.grid_width // 2, self.grid_height // 2, load_xml("resources/xml/player.xml"), self)
        ]

    def add_event(self, ev) -> None:
        self.events.append(ev)

    def clear_events(self) -> None:
        self.events.clear()

    def tick(self) -> None:
        for o in self.objects:
            o.tick()
            if o.active:
                o.draw()