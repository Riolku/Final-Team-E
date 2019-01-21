from game_object import GameObject
from constants import FPS


class Entity(GameObject):
    def __init__(self, x : float, y : float, xml_data, driver, image = None):
        self.xml_data = xml_data
        GameObject.__init__(self, x, y, int(xml_data.get('width')),
                            int(xml_data.get('height')), driver, image_path = xml_data.get('img', ""), image = image
                            )
        self.hp = int(xml_data.get('health'))
        self.v = float(xml_data.get('speed'))
        self.activate()
        self.invincible_timer = 0

    def move(self, dx: float, dy: float) -> None:
        self.x += self.v * dx / FPS
        self.y += self.v * dy / FPS

    def take_damage(self, dmg : int) -> bool:
        # Subtract from HP if they aren't currently invincible
        if not self.invincible_timer:
            print("Ow")
            self.hp -= dmg
            self.invincible_timer = FPS
            return True
        return False

    def tick(self) -> None:
        # Subtract from their invincibility timer
        if self.invincible_timer:
            self.invincible_timer -= 1
