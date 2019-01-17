
# import libraries
import pygame
from constants import SCREEN_SIZE, TILE_SIZE, MAP_WIDTH, MAP_HEIGHT
from player import Player
from game_object import GameObject
from xml_utils import load_xml


class MainDriver:
    # initialize class
    def __init__(self, screen):
        # controls how held keys are repeated. The first number is the delay in milliseconds, the second is the interval
        # at which the keys are repeated
        pygame.key.set_repeat(1, 1)
        # sets screen
        self.screen = screen
        # creates an empty array called events
        self.events = []
        # sets map width
        self.map_width = SCREEN_SIZE[0] * MAP_WIDTH // TILE_SIZE
        # sets map height
        self.map_height = SCREEN_SIZE[1] * MAP_HEIGHT // TILE_SIZE
        # sets screen width
        self.screen_width = SCREEN_SIZE[0] // TILE_SIZE
        # sets screen height
        self.screen_height = SCREEN_SIZE[1] // TILE_SIZE
        # sets background sprite path
        background = pygame.image.load("resources/graphics/forest.png")
        # scales background using the path defined above as the background
        self.background = pygame.transform.scale(background, SCREEN_SIZE)
        # where camera is on the screen, x position
        self.x_offset = (MAP_WIDTH - 1) * self.screen_width // 2
        # where camera is on the screen, y position
        self.y_offset = (MAP_HEIGHT - 1) * self.screen_height // 2
        # creates an empty array called objects
        self.objects = []
        # variable that determines player location and xml
        p = Player(self.map_width // 2, self.map_height // 2, load_xml("resources/xml/player.xml"), self)
        # appends the player to objects
        self.objects.append(p)
        # sets path for rock xml
        rock_xml = load_xml("resources/xml/rock.xml")
        # rock sprite directory is set up
        rock = pygame.image.load("resources/graphics/rock.png")
        w = int(rock_xml.get('width'))
        h = int(rock_xml.get('height'))
        for x in range(self.screen_width, self.screen_width * (MAP_WIDTH - 1), w):
            self.objects.append(GameObject(x, self.screen_height, w, h, self, image = rock, active = True))
            self.objects.append(GameObject(x, self.screen_height * (MAP_HEIGHT - 1), w, h, self, image = rock, active = True))

        for y in range(self.screen_height, self.screen_height * (MAP_HEIGHT - 1), h):
            self.objects.append(GameObject(self.screen_width, y, w, h, self, image = rock, active = True))
            self.objects.append(GameObject(self.screen_width * (MAP_WIDTH - 1), y, w, h, self, image = rock, active = True))

    def add_event(self, ev) -> None:
        # appends parameter 'ev' to self.events
        self.events.append(ev)

    def clear_events(self) -> None:
        # clears events
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
            if not o.active or not o.onscreen():
                continue
            old_x = o.x
            old_y = o.y
            o.tick()
            for o2 in self.objects:
                if o != o2 and o2.active and o2.onscreen() and (o.collides(o2) or o2.collides(o)):
                    o.set_pos(old_x, old_y)
                    break
            else:
                if isinstance(o, Player):
                    dx = o.x - old_x
                    dy = o.y - old_y
                    self.x_offset += dx
                    self.y_offset += dy

            o.draw()
