# Class for the player class and sword

# import libraries
import pygame
from entity import Entity
from weapons import Weapon
from constants import FPS


class Player(Entity):
    # Call super constructor
    def __init__(self, x : float, y : float, xml_data, driver):
        Entity.__init__(self, x, y, xml_data, driver)
        self.sword = PlayerSword(self, xml_data.find('sword'), driver)
        self.driver.objects.append(self.sword)
        self.using_sword = False

    def tick(self):
        Entity.tick(self)

        # Player movement based on driver events
        for ev in self.driver.events:
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_w:
                    self.move(0, -1)
                    self.set_direction((0, -1))
                elif ev.key == pygame.K_a:
                    self.move(-1, 0)
                    self.set_direction((-1, 0))
                elif ev.key == pygame.K_d:
                    self.move(1, 0)
                    self.set_direction((1, 0))
                elif ev.key == pygame.K_s:
                    self.move(0, 1)
                    self.set_direction((0, 1))

            # Stop using sword
            if ev.type == pygame.MOUSEBUTTONUP:
                self.using_sword = False
                self.sword.deactivate()

            # Use sword
            elif ev.type == pygame.MOUSEBUTTONDOWN:
                self.using_sword = True

        # Call the sword "use" function
        if self.using_sword:
            self.sword.use()

    # Move the player
    # If they arent using the sword, call the super method
    def move(self, dx : float, dy : float) -> None:
        if not self.using_sword:
            Entity.move(self, dx, dy)


# Player sword class
class PlayerSword(Weapon):
    # Call super constructor
    def __init__(self, wielder : Player, xml_data, driver):
        Weapon.__init__(self, xml_data, driver)
        self.wielder = wielder

    def use(self) -> None:
        # Set the direction and position based on direction
        self.set_direction(self.wielder.direction)
        midx = self.wielder.left_edge() + self.wielder.width // 2
        midy = self.wielder.top_edge() + self.wielder.height // 2
        if self.direction == (1, 0):
            self.set_pos(self.wielder.right_edge(), midy - self.width // 2)
        elif self.direction == (0, -1):
            self.set_pos(midx - self.width // 2, self.wielder.top_edge() - self.height)
        elif self.direction == (-1, 0):
            self.set_pos(self.wielder.left_edge() - self.height, midy - self.width // 2)
        else:
            self.set_pos(midx - self.width // 2, self.wielder.bottom_edge())

        # Activate the sword
        self.activate()