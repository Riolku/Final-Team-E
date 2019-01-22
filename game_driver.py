import pygame
from constants import SCREEN_SIZE, TITLE, REPEAT_DELAY, REPEAT_INTERVAL
from main_driver import MainDriver

pygame.font.init()

BACKGROUND = (0, 0, 0)
BLACK = (0, 0, 0)
TEXT_COLOUR = (0, 0, 0)
BUTTON_COLOUR = (100, 0, 110)
BUTTON_COLOUR_HIGHLIGHT = (120, 72, 124)

font_big = pygame.font.SysFont(None, 100)
font_small = pygame.font.SysFont(None, 20)

class GameDriver:
    def __init__(self):
        pygame.key.set_repeat(REPEAT_DELAY, REPEAT_INTERVAL)
        # TODO: Start in init state
        self.state = "main"
        self.events = []
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        pygame.display.set_caption(TITLE)
        self.main_driver = MainDriver(self, self.screen)

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
            self.gameOver = font_big.render("Game Over!", True, TEXT_COLOUR, self.screen)
            self.gameOverRect = self.gameOver.get_rect()
            self.gameOverRect.centerx = self.screen.get_rect().centerx
            self.gameOverRect.centery = self.screen.get_rect().centery
            self.screen.blit(self.gameOver, self.gameOverRect)


