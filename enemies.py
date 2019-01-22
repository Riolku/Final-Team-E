from entity import Entity
from constants import FPS
import math


class Enemy(Entity):
    def __init__(self, x, y, xml_data, driver, image = None):
        self.dmg = int(xml_data.get("dmg"))
        Entity.__init__(self, x, y, xml_data, driver, image = image)
        self.player = driver.player
        self.stun_time = 0

    def deal_damage(self) -> None:
        self.player.take_damage(self.dmg)

    def tick(self) -> None:
        Entity.tick(self)

        self.stun_time -= 1
        if self.stun_time > 0:
            return

        dx = self.player.x - self.x
        dy = self.player.y - self.y
        hypot = math.hypot(dx, dy)

        x_move = dx / hypot
        y_move = dy / hypot
        self.move(x_move, y_move)

    def take_damage(self, dmg : int) -> None:
        # Call the super method
        took_damage = Entity.take_damage(self, dmg)

        if took_damage:
            # Set a stunned timer
            self.stun_time = FPS // 2


class Zombie(Enemy):
    def tick(self):
        Enemy.tick(self)
        if self.collides(self.player):
            self.deal_damage()