import pygame
from game_driver import GameDriver
from constants import FPS
import atexit, traceback

def healthbar(surface, max_health_color, current_health_color, x, y, current_health, max_health, health_bar_height):

    # draws the health bar at max value
    pygame.draw.rect(surface, max_health_color, (x, y, max_health, health_bar_height), 0)

    # draws the health bar at current value
    pygame.draw.rect(surface, current_health_color, (x, y, int(max(min(current_health / float(max_health) * max_health, max_health), 0)), health_bar_height), 0)

@atexit.register
def when_die():
    traceback.print_exc()

pygame.init()

driver = GameDriver()

run = True
while run:
    pygame.time.delay(1000 // FPS)
    driver.clear_events()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        driver.add_event(event)

    driver.screen.fill((255, 255, 255))
    driver.tick()
    # Parameters: screen, max health color, current health color, x-pos, y-pos, current health value, max health value, health bar height
    healthbar(driver.screen, (128,128,128), (255,0,0), 10, 650, 100, 200, 20)
    pygame.display.flip()


pygame.quit()
