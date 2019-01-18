import pygame
from game_driver import GameDriver
from constants import FPS
import atexit, traceback


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
    pygame.display.flip()

pygame.quit()
