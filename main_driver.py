import pygame
from constants import SCREEN_SIZE, TILE_SIZE, TILEX_BUFFER, TILEY_BUFFER
from player import Player
from xml_utils import load_xml, write_xml


class MainDriver:
    def __init__(self, screen):
        pygame.key.set_repeat(1, 1)
        self.screen = screen
        self.events = []
        self.grid_width = SCREEN_SIZE[0] // TILE_SIZE - TILEX_BUFFER
        self.grid_height = SCREEN_SIZE[1] // TILE_SIZE - TILEY_BUFFER
        self.grid = [
            [
                None for _ in range(self.grid_width)
            ]
            for _ in range(self.grid_height)
        ]
        self.objects = []
        p = Player(self.grid_width // 2, self.grid_height // 2, load_xml("resources/xml/player.xml"), self)
        self.objects.append(p)

    def add_event(self, ev) -> None:
        self.events.append(ev)

    def clear_events(self) -> None:
        self.events.clear()

    def tick(self) -> None:
        for o in self.objects:
            old_x = o.x
            old_y = o.y
            o.tick()
            if o.x < 0:
                o.set_pos(0, o.y)
            if o.x >= self.grid_width:
                o.set_pos(self.grid_width - 1, o.y)
            if o.y < 0:
                o.set_pos(o.x, 0)
            if o.y >= self.grid_height:
                o.set_pos(o.x, self.grid_height - 1)

            if self.grid[o.y][o.x] is None:
                self.grid[o.y][o.x] = o
                self.grid[old_y][old_x] = None

            if o.active:
                o.draw()
