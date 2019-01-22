# File for the game_driver

# import libraries
import pygame
from constants import SCREEN_SIZE, TITLE, REPEAT_DELAY, REPEAT_INTERVAL, TEXT_COLOUR, font_big, font_small
from main_driver import MainDriver

# initialize font
pygame.font.init()


class GameDriver:
    def __init__(self):
        # Initialize the state to main state
        self.state = "main"

        # Store the pygame events
        self.events = []

        # Initialize the pygame screen
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)

        # Initialize the main_driver
        self.main_driver = MainDriver(self, self.screen)

        # Game over attributes
        self.gameOver = font_big.render("Game Over!", True, TEXT_COLOUR, self.screen)
        self.gameOverRect = self.gameOver.get_rect()
        self.gameOverRect.centerx = self.screen.get_rect().centerx
        self.gameOverRect.centery = self.screen.get_rect().centery

    def add_event(self, ev) -> None:
        self.events.append(ev)
        if self.state == "main":
            self.main_driver.add_event(ev)

    def clear_events(self) -> None:
        self.events.clear()
        self.main_driver.clear_events()

    def tick(self) -> None:
        if self.state == "main":
            self.main_driver.tick()
        elif self.state == "game_over":
            self.screen.blit(self.gameOver, self.gameOverRect)

            self.scoreText = font_small.render("Your score was:", True, TEXT_COLOUR, self.screen)
            self.screen.blit(self.scoreText, (200,400))
            self.screen.blit(self.main_driver.scoreText, (480,400))


