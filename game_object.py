import pygame
from constants import TILE_SIZE


class GameObject:
    def __init__(self, x : float, y : float, w : int, h : int, driver, image_path : str = "", image = None, active = False):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        if image is None:
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
        self.active = active
        self.driver = driver

    def onscreen(self) -> bool:
        x = self.x - self.driver.x_offset
        y = self.y - self.driver.y_offset
        x_in = 0 <= x < self.driver.screen_width or 0 <= x + self.width < self.driver.screen_width
        y_in = 0 <= y < self.driver.screen_height or 0 <= y + self.width < self.driver.screen_height
        return x_in and y_in

    def draw(self) -> None:
        x = self.x - self.driver.x_offset
        y = self.y - self.driver.y_offset
        if self.onscreen():
            self.driver.screen.blit(self.image, (x * TILE_SIZE, y * TILE_SIZE))

    def set_pos(self, x : float, y : float) -> None:
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

    def left_edge(self) -> float:
        return self.x

    def right_edge(self) -> float:
        return self.x + self.width

    def top_edge(self) -> float:
        return self.y

    def bottom_edge(self) -> float:
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
