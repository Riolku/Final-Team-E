from game_object import GameObject
from entity import Entity


class Weapon(GameObject):
    def __init__(self, xml_data, driver):
        self.damage = int(xml_data.get('dmg'))
        GameObject.__init__(self, 0, 0, int(xml_data.get('width')), int(xml_data.get('height')),
                            driver, image_path = xml_data.get('img'))

    def deal_damage(self, target : Entity) -> None:
        target.hp -= self.damage

    def use(self):
        raise NotImplementedError

