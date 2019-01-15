import pygame
from constants import TILE_SIZE


class GameObject:
    def __init__(self, x : int, y : int, w : int, h : int, image_path : str, driver):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        image = pygame.image.load(image_path)
        orig_image = pygame.transform.scale(image, (w * TILE_SIZE, h * TILE_SIZE))
        self.images = [
            pygame.transform.rotate(orig_image, 270),
            orig_image,
            pygame.transform.rotate(orig_image, 90),
            pygame.transform.rotate(orig_image, 180)
        ]
        self.image = orig_image
        self.direction = (0, -1)
        self.active = False
        self.driver = driver

    def draw(self) -> None:
        self.driver.screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def set_pos(self, x : int, y : int) -> None:
        self.x = x
        self.y = y

    def set_direction(self, new_direction : tuple) -> None:
        self.direction = new_direction
        if self.direction == (1, 0):
            self.image = self.images[0]
        elif self.direction == (0, -1):
            self.image = self.images[1]
        elif self.direction == (-1, 0):
            self.image = self.images[2]
        else:
            self.image = self.images[3]

    def left_edge(self) -> int:
        return self.x

    def right_edge(self) -> int:
        return self.x + self.width

    def top_edge(self) -> int:
        return self.y

    def bottom_edge(self) -> int:
        return self.y + self.height

    def inside(self, point : tuple) -> bool:
        return self.x <= point[0] <= self.x + self.width and self.y <= point[1] <= self.y + self.height

    def collides(self, other) -> bool:
        return any(self.inside((other.x + other.width * cw, other.y + other.height * ch))
                   for cw in range(2)
                   for ch in range(2))

    def activate(self) -> None:
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def tick(self) -> None:
        pass
