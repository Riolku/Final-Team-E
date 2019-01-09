import pygame
from xml_utils import load_xml, write_xml


class GameObject:
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = pygame.transform.scale(image, (w, h))

    def draw(self):
        pygame.display.get_surface().blit(self.image, (self.x, self.y))

    def set_pos(self, x, y):
        self.x = x
        self.y = y


class Entity(GameObject):
    def __init__(self, x, y, xml_data):
        self.xml_data = xml_data
        GameObject.__init__(self, x, y, int(xml_data.find('width').text),
                            int(xml_data.find('height').text), xml_data.find('image').text)
        self.v = int(xml_data.v)

    def move(self, dx, dy):
        self.x += self.v * dx
        self.y += self.v * dy


class Player(Entity):
    def __init__(self, x, y, xml_data):
        Entity.__init__(self, x, y, xml_data)

    # def use_sword(self):

    # def use_bow(self):


class Enemy(Entity):
    def __init__(self, x, y, xml_data):
        Entity.__init__(self, x, y, xml_data)


