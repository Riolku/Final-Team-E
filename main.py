# Main pygame loop file

# import libraries
import pygame
from game_driver import GameDriver
from constants import FPS
import start_screen

# Initialize pygame
pygame.init()

# initialize game driver
driver = GameDriver()

# run the start screen
start_screen.game_intro()

# Main pygame loop
run = True
while run:
    pygame.time.delay(1000 // FPS)

    # Clear previous driver events
    driver.clear_events()

    # Add driver events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break
        driver.add_event(event)

    # Clear the screen
    driver.screen.fill((255, 255, 255))

    # Make sure the game is still running
    run = run and driver.tick()

    # Update the screen
    pygame.display.flip()

# Quit pygame
pygame.quit()
