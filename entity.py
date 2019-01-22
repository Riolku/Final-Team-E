# File for the base entity class

# Import libraries
from game_object import GameObject
from constants import FPS


class Entity(GameObject):
    def __init__(self, x : float, y : float, xml_data, driver, image = None):
        self.xml_data = xml_data
        # Call the super constructor
        GameObject.__init__(self, x, y, int(xml_data.get('width')),
                            int(xml_data.get('height')), driver, image_path = xml_data.get('img', ""), image = image
                            )
        # Initialize their hp and speed
        self.hp = int(xml_data.get('health'))
        self.v = float(xml_data.get('speed'))

        # Activate the entity
        self.activate()

        # Set an invincible timer, which happens after they take damage
        self.invincible_timer = 0

    # Method to move the entity
    def move(self, dx: float, dy: float) -> None:
        self.x += self.v * dx / FPS
        self.y += self.v * dy / FPS

    # Method to take damage
    def take_damage(self, dmg : int) -> bool:
        # Subtract from HP if they aren't currently invincible
        if not self.invincible_timer:
            self.hp -= dmg
            self.invincible_timer = FPS // 3

            # If they have less than or equal to 0 hp, destroy them
            if self.hp <= 0:
                self.destroy()

            return True
        return False

    # Generic tick method
    def tick(self) -> None:
        # Subtract from their invincibility timer
        if self.invincible_timer:
            self.invincible_timer -= 1
