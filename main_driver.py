import pygame
from constants import SCREEN_SIZE, TILE_SIZE, MAP_WIDTH, MAP_HEIGHT
from player import Player
from xml_utils import load_xml


class MainDriver:
    def __init__(self, screen):
        pygame.key.set_repeat(1, 1)
        self.screen = screen
        self.events = []
        self.map_width = SCREEN_SIZE[0] * MAP_WIDTH // TILE_SIZE
        self.map_height = SCREEN_SIZE[1] * MAP_HEIGHT // TILE_SIZE
        self.screen_width = SCREEN_SIZE[0] // TILE_SIZE
        self.screen_height = SCREEN_SIZE[1] // TILE_SIZE
        background = pygame.image.load("resources/graphics/forest.png")
        self.background = pygame.transform.scale(background, SCREEN_SIZE)
        self.map = [
            [
                None for _ in range(self.map_width)
            ]
            for _ in range(self.map_height)
        ]
        self.rock = pygame.image.load("resources/graphics/rock.png")
        self.x_offset = (MAP_WIDTH - 1) * self.screen_width // 2
        self.y_offset = (MAP_HEIGHT - 1) * self.screen_height // 2
        self.objects = []
        p = Player(self.map_width // 2, self.map_height // 2, load_xml("resources/xml/player.xml"), self)
        self.objects.append(p)

    def add_event(self, ev) -> None:
        self.events.append(ev)

    def clear_events(self) -> None:
        self.events.clear()

    def tick(self) -> None:
        for tilex in range(MAP_WIDTH):
            for tiley in range(MAP_HEIGHT):
                x = (self.screen_width * tilex - self.x_offset)
                y = (self.screen_height * tiley - self.y_offset)
                if (0 <= x < self.screen_width or 0 <= x + self.screen_width < self.screen_width) \
                    and \
                    (0 <= y < self.screen_height or 0 <= y + self.screen_height < self.screen_height):
                    self.screen.blit(self.background, (x * TILE_SIZE, y * TILE_SIZE))

        for o in self.objects:
            old_x = o.x
            old_y = o.y
            o.tick()
            if o.x < 0:
                o.set_pos(0, o.y)
            if o.x >= self.map_width:
                o.set_pos(self.map_width - 1, o.y)
            if o.y < 0:
                o.set_pos(o.x, 0)
            if o.y >= self.map_height:
                o.set_pos(o.x, self.map_height - 1)

            if self.map[o.y][o.x] is None:
                self.map[o.y][o.x] = o
                self.map[old_y][old_x] = None

            if o.active:
                o.draw()
