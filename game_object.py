# File for the generic game object

# Import libraries
import pygame
from constants import TILE_SIZE


class GameObject:
    # Pass the position, width & height, related driver
    # Also pass the image or the image_path
    # active is false by default
    def __init__(self, x : float, y : float, w : int, h : int, driver, image_path : str = "", image = None, active = False):
        # Set the position and width and height
        self.x = x
        self.y = y
        self.width = w
        self.height = h

        # Load the image
        if image is None:
            image = pygame.image.load(image_path)

        # scale the image
        orig_image = pygame.transform.scale(image, (w * TILE_SIZE, h * TILE_SIZE))

        # Store all the rotations of the images
        self.images = [
            pygame.transform.rotate(orig_image, 270),
            orig_image,
            pygame.transform.rotate(orig_image, 90),
            pygame.transform.rotate(orig_image, 180)
        ]

        # Store the current image
        self.image = orig_image

        # Whether the object still exists
        self.exists = True

        # The direction the object is facing. Default up
        self.direction = (0, -1)

        # Store the driver and whether the object is active
        self.active = active
        self.driver = driver

    # Determine if the object is on the screen
    def onscreen(self) -> bool:
        # Get the relative x and ys
        x = self.x - self.driver.x_offset
        y = self.y - self.driver.y_offset

        # Determine if any corner is on the screen
        x_in = 0 <= x < self.driver.screen_width or 0 <= x + self.width < self.driver.screen_width
        y_in = 0 <= y < self.driver.screen_height or 0 <= y + self.width < self.driver.screen_height
        return x_in and y_in

    # Draw the object
    def draw(self) -> None:
        # Get the relative x and y
        dx = self.driver.x_offset
        dy = self.driver.y_offset
        x = self.x - dx
        y = self.y - dy
        if self.onscreen():
            # Put the current image on the screen
            # Multiply by tile size to scale to the screen
            self.driver.screen.blit(self.image, (x * TILE_SIZE, y * TILE_SIZE))

    # Set the position of the object
    def set_pos(self, x : float, y : float) -> None:
        self.x = x
        self.y = y

    # Set the direction of the object
    # Set the current image as well
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

    # Methods determining the edges of the object
    def left_edge(self) -> float:
        return self.x

    def right_edge(self) -> float:
        if self.direction[0]:
            # They are facing left or right
            return self.x + self.height
        return self.x + self.width

    def top_edge(self) -> float:
        return self.y

    def bottom_edge(self) -> float:
        if self.direction[0]:
            # They are facing left or right
            return self.y + self.width
        return self.y + self.height

    # Whether this object collides with another one
    def collides(self, other) -> bool:
        collide_left = max(self.left_edge(), other.left_edge())
        collide_right = min(self.right_edge(), other.right_edge())
        collide_top = max(self.top_edge(), other.top_edge())
        collide_bottom = min(self.bottom_edge(), other.bottom_edge())
        return collide_left < collide_right and collide_top < collide_bottom

    # Destroy the current object
    def destroy(self) -> None:
        self.exists = False

    # Activate the object
    def activate(self) -> None:
        self.active = True

    # De-activate the object
    def deactivate(self) -> None:
        self.active = False

    # The generic tick method, called every frame
    # By default, do nothing
    def tick(self) -> None:
        pass
