import pygame

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
    def __init__(self, x, y, w, h, v, image):
        GameObject.__init__(self, x, y, w, h, image)
        self.v = v

    def move(self, dx, dy):
        self.x += self.v * dx
        self.y += self.v * dy


class Player(Entity):
    def __init__(self, x, y, w, h, v, image):
        Entity.__init__(self, x, y, w, h, v, image)

    # def use_sword(self):

    # def use_bow(self):


class Enemy(Entity):
    def __init__(self, xml_file):
        Entity.__init__(self, x, y, v, image)

