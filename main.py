import pygame
from game_driver import GameDriver
from constants import FPS

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
pygame.quit()