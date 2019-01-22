
# import libraries
import pygame
from random import randint as rint
from constants import SCREEN_SIZE, TILE_SIZE, MAP_WIDTH, MAP_HEIGHT, FPS
from player import Player, PlayerSword
from game_object import GameObject
from xml_utils import load_xml
from enemies import Zombie, Enemy
from entity import Entity
from math import log2


class MainDriver:
    # initialize class
    def __init__(self, parent, screen):
        # controls how held keys are repeated. The first number is the delay in milliseconds, the second is the interval
        # at which the keys are repeated
        pygame.key.set_repeat(1, 1)

        # Set the parent driver
        self.parent = parent

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
        self.player = Player(self.map_width // 2, self.map_height // 2, load_xml("resources/xml/player.xml"), self)
        # appends the player to objects
        self.objects.append(self.player)
        # load the rock xml
        rock_xml = load_xml("resources/xml/rock.xml")
        # rock sprite directory is set up
        rock = pygame.image.load("resources/graphics/rock.png")
        # width of the rock
        w = int(rock_xml.get('width'))
        # height of the rock
        h = int(rock_xml.get('height'))
        # path to zombie image
        self.zombie_img = pygame.image.load("resources/graphics/enemies/zombie.png")
        # makes rocks appear at a certain boundary on the top and bottom (x axis)
        for x in range(self.screen_width, self.screen_width * (MAP_WIDTH - 1), w):
            self.objects.append(GameObject(x, self.screen_height, w, h, self, image = rock, active = True))
            self.objects.append(GameObject(x, self.screen_height * (MAP_HEIGHT - 1), w, h, self, image = rock, active = True))
        # makes rocks appear at a certain boundary on the left and right (y axis)
        for y in range(self.screen_height, self.screen_height * (MAP_HEIGHT - 1), h):
            self.objects.append(GameObject(self.screen_width, y, w, h, self, image = rock, active = True))
            self.objects.append(GameObject(self.screen_width * (MAP_WIDTH - 1), y, w, h, self, image = rock, active = True))

        # Preload the xml so we can reuse it
        self.zombie_xml = load_xml("resources/xml/zombie.xml")

        # Set a score value, initially 0
        self.score = 0

    def add_event(self, ev) -> None:
        # appends parameter 'ev' to self.events
        self.events.append(ev)

    def clear_events(self) -> None:
        # clears events
        self.events.clear()

    def spawn_enemies(self) -> None:
        # Roll a dice to see if enemy should spawn
        # Use the current score: the more score, the less seconds before an enemy spawns
        # This variable stores the average number of seconds before a zombie will spawn
        seconds = -log2(self.score + 1) / log2(6) + 2.4

        # Roll the dice
        dice_roll = rint(1, max(FPS // 5, int(seconds * FPS)))
        # if dice roll is not equal to 1, end
        if dice_roll != 1:
            return

        # Spawn an enemy at random location
        x = rint(0, (MAP_WIDTH - 1) * self.screen_width)
        y = rint(0, (MAP_HEIGHT - 1) * self.screen_height)
        e = Zombie(x, y, self.zombie_xml, self, image = self.zombie_img)
        # Make sure they aren't on screen
        # If they were on screen, an enemy would just "pop" into existence
        while e.onscreen():
            x = rint(0, (MAP_WIDTH - 1) * self.screen_width)
            y = rint(0, (MAP_HEIGHT - 1) * self.screen_height)
            e.set_pos(x, y)
        e.activate()
        self.objects.append(e)

    def tick(self) -> None:
        self.spawn_enemies()
        for tilex in range(MAP_WIDTH):
            for tiley in range(MAP_HEIGHT):
                x = (self.screen_width * tilex - self.x_offset)
                y = (self.screen_height * tiley - self.y_offset)
                if (0 <= x < self.screen_width or 0 <= x + self.screen_width < self.screen_width) \
                    and \
                    (0 <= y < self.screen_height or 0 <= y + self.screen_height < self.screen_height):
                    self.screen.blit(self.background, (x * TILE_SIZE, y * TILE_SIZE))

        for o in self.objects:
            if not o.active:
                continue

            if not isinstance(o, Entity):
                continue

            old_x = o.x
            old_y = o.y
            o.tick()
            for o2 in self.objects:
                if o != o2 and o2.active and o.collides(o2):
                    o.set_pos(old_x, old_y)
                    break
            else:
                if isinstance(o, Player):
                    dx = o.x - old_x
                    dy = o.y - old_y
                    self.x_offset += dx
                    self.y_offset += dy

        new_objects = []
        for o in self.objects:
            if isinstance(o, Enemy):
                if self.player.sword.active and o.collides(self.player.sword):
                    self.player.sword.deal_damage(o)
                    if not o.exists:
                        self.score += 1
                        continue

            new_objects.append(o)

            if o.active:
                o.draw()

        self.objects = new_objects

        if not self.player.exists:
            self.parent.state = "game_over"
