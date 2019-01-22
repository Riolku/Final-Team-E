# File for the generic weapon class
# Implements generic methods

# Import libraries
from game_object import GameObject
from entity import Entity


class Weapon(GameObject):
    # Default passes the XML of the weapon and the driver
    def __init__(self, xml_data, driver):
        self.dmg = int(xml_data.get('dmg'))

        # call the super constructor
        GameObject.__init__(self, 0, 0, int(xml_data.get('width')), int(xml_data.get('height')),
                            driver, image_path = xml_data.get('img'))

    # Generic deal_damage method
    def deal_damage(self, target : Entity) -> None:
        target.take_damage(self.dmg)

    # use is not implemented by default
    def use(self):
        raise NotImplementedError

