from entity import Entity
from weapons import Weapon


class Player(Entity):
    def __init__(self, x, y, xml_data):
        Entity.__init__(self, x, y, xml_data)
        self.sword = PlayerSword(self, xml_data.find('sword'))
        self.bow = PlayerBow(self, xml_data.find('bow'))

    def use_sword(self):
        self.sword.use()

    # def use_bow(self):


class PlayerSword(Weapon):
    def __init__(self, wielder : Player, xml_data):
        Weapon.__init__(self, xml_data)
        self.wielder = wielder

    def use(self) -> None:
        self.set_direction(self.wielder.direction)
        midx = self.wielder.left_edge() + self.wielder.width // 2
        midy = self.wielder.top_edge() + self.wielder.height // 2
        if self.direction == (1, 0):
            self.set_pos(self.wielder.right_edge(), midy + self.height // 2)
        elif self.direction == (0, -1):
            self.set_pos(midx - self.width // 2, self.wielder.bottom_edge())
        elif self.direction == (-1, 0):
            self.set_pos(self.wielder.left_edge() + self.width, midy - self.height // 2)
        else:
            self.set_pos(midx - self.width, self.wielder.top_edge() - self.height)
        self.activate()


class PlayerBow(Weapon):
    def __init__(self, wielder : Player, xml_data):
        Weapon.__init__(self, xml_data)
        self.wielder = wielder

    # def use(self) -> None:
