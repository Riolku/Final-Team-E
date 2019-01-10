from objects import GameObject, PlayerSword


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


class Player(Entity):
    def __init__(self, x, y, xml_data):
        Entity.__init__(self, x, y, xml_data)
        self.sword = PlayerSword()

    # def use_sword(self):

    # def use_bow(self):


class Enemy(Entity):
    def __init__(self, x, y, xml_data):
        self.damage = int(xml_data.get("dmg"))
        Entity.__init__(self, x, y, xml_data)

    def deal_damage(self, other : Player) -> None:
        other.take_damage(self.damage)