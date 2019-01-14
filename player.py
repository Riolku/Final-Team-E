import pygame
from entity import Entity
from weapons import Weapon


class Player(Entity):
    def __init__(self, x, y, xml_data, driver):
        Entity.__init__(self, x, y, xml_data, driver)
        self.sword = PlayerSword(self, xml_data.find('sword'), driver)
        # self.bow = PlayerBow(self, xml_data.find('bow'))
        self.driver.objects.append(self.sword)

    def use_sword(self):
        self.sword.use()

    # def use_bow(self):
    def tick(self):
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
            if ev.type == pygame.MOUSEBUTTONDOWN:
                self.use_sword()


class PlayerSword(Weapon):
    def __init__(self, wielder : Player, xml_data, driver):
        Weapon.__init__(self, xml_data, driver)
        self.wielder = wielder

    def use(self) -> None:
        self.set_direction(self.wielder.direction)
        midx = self.wielder.left_edge() + self.wielder.width // 2
        midy = self.wielder.top_edge() + self.wielder.height // 2
        print(self.wielder.x, self.wielder.y)
        print(self.wielder.right_edge())
        if self.direction == (1, 0):
            self.set_pos(self.wielder.right_edge(), midy - self.width // 2)
        elif self.direction == (0, -1):
            self.set_pos(midx - self.width // 2, self.wielder.top_edge() - self.height)
        elif self.direction == (-1, 0):
            self.set_pos(self.wielder.left_edge() - self.height, midy - self.width // 2)
        else:
            self.set_pos(midx - self.width // 2, self.wielder.bottom_edge())
        self.activate()


class PlayerBow(Weapon):
    def __init__(self, wielder : Player, xml_data, driver):
        Weapon.__init__(self, xml_data, driver)
        self.wielder = wielder

    # def use(self) -> None:
