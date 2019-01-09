import pygame

class GameObject:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self):
        pygame.display.get_surface().blit(self.image, (self.x, self.y))

    def set_pos(self, x, y):
        self.x = x
        self.y = y


class Entity(GameObject):
    def __init__(self, x, y, v, image):
        GameObject.__init__(self, x, y, image)
        self.v = v

    def move(self, dx, dy):
        self.x += self.v * dx
        self.y += self.v * dy


class Player(Entity):
    def __init__(self, x, y, v, image):
        Entity.__init__(self, x, y, v, image)

    # def use_sword(self):

    # def use_bow(self):


class Enemy(Entity):
    def __init__(self, x, y, v, image):
        Entity.__init__(self, x, y, v, image)

