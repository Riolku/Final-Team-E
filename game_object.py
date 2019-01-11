import pygame


class GameObject:
    def __init__(self, x, y, w, h, image):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        orig_image = pygame.transform.scale(image, (w, h))
        self.images = [
            orig_image,
            pygame.transform.rotate(orig_image, 90),
            pygame.transform.rotate(orig_image, 180),
            pygame.transform.rotate(orig_image, 270)
        ]
        self.image = orig_image
        self.direction = (1, 0)
        self.active = False

    def draw(self) -> None:
        pygame.display.get_surface().blit(self.image, (self.x, self.y))

    def set_pos(self, x, y) -> None:
        self.x = x
        self.y = y

    def set_direction(self, new_direction) -> None:
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
