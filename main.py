import pygame
from game_driver import GameDriver
from constants import FPS
import atexit, traceback
import start_screen
import health

@atexit.register
def when_die():
    traceback.print_exc()

pygame.init()

driver = GameDriver()
start_screen.game_intro()

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
    health.healthbar(driver.screen, (128,128,128), (255,0,0), 10, 650, 100, 200, 20)
    pygame.display.flip()


pygame.quit()
