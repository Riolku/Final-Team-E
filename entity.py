from game_object import GameObject


class Entity(GameObject):
    def __init__(self, x, y, xml_data):
        self.xml_data = xml_data
        GameObject.__init__(self, x, y, int(xml_data.get('width')),
                            int(xml_data.get('height')), xml_data.get('img'))
        self.hp = int(xml_data.get('health'))
        self.v = int(xml_data.get('speed'))

    def move(self, dx, dy) -> None:
        self.x += self.v * dx
        self.y += self.v * dy

    def take_damage(self, dmg : int) -> None:
        self.hp -= dmg
