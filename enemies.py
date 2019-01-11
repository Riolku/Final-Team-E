from entity import Entity
from player import Player


class Enemy(Entity):
    def __init__(self, x, y, xml_data):
        self.damage = int(xml_data.get("dmg"))
        Entity.__init__(self, x, y, xml_data)

    def deal_damage(self, other : Player) -> None:
        other.take_damage(self.damage)