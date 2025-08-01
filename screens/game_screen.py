import pygame
import sys

def draw_game_screen(screen, width, height, cannon_x, cannon_y):
    BLACK = (0, 0, 0)
    GREEN = (0, 255, 0)

    screen.fill(BLACK)
    pygame.draw.rect(screen, GREEN, (cannon_x, cannon_y, 40, 20))
    pygame.display.flip()
