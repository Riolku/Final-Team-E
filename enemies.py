# Class for the generic enemy class and the Zombie class

# Import libraries
from entity import Entity
from constants import FPS
import math


class Enemy(Entity):
    # Load the damage from the xml file and call the super constructor
    def __init__(self, x, y, xml_data, driver, image = None):
        self.dmg = int(xml_data.get("dmg"))
        Entity.__init__(self, x, y, xml_data, driver, image = image)

        # Initialize the player as their target
        self.player = driver.player

        # Stun-time, how long they are stunned on hit
        self.stun_time = 0

    # Deal damage to the player
    def deal_damage(self) -> None:
        self.player.take_damage(self.dmg)

    def tick(self) -> None:
        # Call the super method
        Entity.tick(self)

        # If they are stunned, do nothing
        self.stun_time -= 1
        if self.stun_time > 0:
            return

        # Otherwise, move towards the player
        dx = self.player.x - self.x
        dy = self.player.y - self.y
        hypot = math.hypot(dx, dy)

        x_move = dx / hypot
        y_move = dy / hypot
        self.move(x_move, y_move)

    # Take damage
    def take_damage(self, dmg : int) -> None:
        # Call the super method
        took_damage = Entity.take_damage(self, dmg)

        # Set a stunned timer if they take damage
        if took_damage:
            # Set a stunned timer
            self.stun_time = FPS // 3


# Zombie enemy class
class Zombie(Enemy):
    def tick(self):
        Enemy.tick(self)
        # If they collide with the player, deal the player damage
        if self.collides(self.player):
            self.deal_damage()