from constants import SCREEN_SIZE, TILE_SIZE
from player import Player
from xml_utils import load_xml, write_xml


class MainDriver:
    def __init__(self):
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
            Player(300, 300, load_xml("resources/xml/player.xml"), self)
        ]

    def add_event(self, ev) -> None:
        self.events.add(ev)

    def clear_events(self) -> None:
        self.events.clear()

    def tick(self) -> None:
        for o in self.objects:
            o.tick()
            if o.active:
                o.draw()