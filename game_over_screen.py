# Final Project: Princess Castle
# Modifications: created function to be called when game is done
# Elina Ho - January 14, 2018

import pygame

pygame.init()

# sets colour to be called later
BACKGROUND = (0, 0, 0)
BLACK = (0, 0, 0)
TEXT_COLOUR = (255, 255, 255)
BUTTON_COLOUR = (100, 0, 110)
BUTTON_COLOUR_HIGHLIGHT = (120, 72, 124)

# set the screen size
screen_width = 600
screen_height = 600
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

# label the window
caption = "Game Over Screen Test"
pygame.display.set_caption(caption)

# sets font
font_big = pygame.font.SysFont(None, 100)
font_small = pygame.font.SysFont(None, 20)

run = True

# Class that prints game over screen and play again button
class Game_Over:
    def __init__(self):
        self.gameOver = font_big.render("Game Over!", True, TEXT_COLOUR, screen)
        self.gameOverRect = self.gameOver.get_rect()
        self.gameOverRect.centerx = screen.get_rect().centerx
        self.gameOverRect.centery = screen.get_rect().centery

    def play_again(self):
        self.playAgain = font_small.render("PLAY AGAIN", True, TEXT_COLOUR, screen)
        self.playAgainRect = self.playAgain.get_rect()
        self.playAgainRect.centerx = screen.get_rect().centerx - 200
        self.playAgainRect.centery = screen.get_rect().centery + 200

# def game_over():
#     gameOver = font_big.render("Game Over!", True, TEXT_COLOUR, screen)
#     gameOverRect = gameOver.get_rect()
#     gameOverRect.centerx = screen.get_rect().centerx
#     gameOverRect.centery = screen.get_rect().centery
#     screen.blit(gameOver, gameOverRect)

# function that displays the "try again" box
# def play_again():
#     playAgain = font_small.render("PLAY AGAIN", True, TEXT_COLOUR, screen)
#     playAgainRect = playAgain.get_rect()
#     playAgainRect.centerx = screen.get_rect().centerx - 200
#     playAgainRect.centery = screen.get_rect().centery + 200
#     screen.blit(playAgain, playAgainRect)

    pygame.display.update()

# while run:
#     for event in pygame.event.get():
#         # checks if something happened
#         if event.type == pygame.QUIT:
#             # run is false means quit program
#             run = False
#         if event.type == pygame.MOUSEBUTTONUP:
#             pos = pygame.mouse.get_pos()
#
#     screen.fill(BACKGROUND)
#
#     pygame.draw.rect(screen, BUTTON_COLOUR, (50, 475, 100, 50))
#
#     mouse = pygame.mouse.get_pos()
#
#     # print(mouse)
#
#     if 50 + 100 > mouse[0] > 50 and 475 + 50 > mouse[1] > 475:
#         pygame.draw.rect(screen, BUTTON_COLOUR_HIGHLIGHT, (50, 475, 100, 50))
#         # link to main screen
#     else:
#         pygame.draw.rect(screen, BUTTON_COLOUR, (50, 475, 100, 50))



    # calls the game over function
    # game_over()
    # game_over = Game_Over()
    # play_again = Game_Over()
    # play_again.play_again()
    # screen.blit(game_over.gameOver, game_over.gameOverRect)
    # screen.blit(play_again.playAgain, play_again.playAgainRect)

    # calls the try again function
    # play_again()

    # flip the graphics onto the screen
    # pygame.display.flip()
    #
    # # Screen Fill
    # screen.fill(BACKGROUND)

# Quits Game
pygame.quit()