import pygame
import sys

def show_game_over_screen(screen, width, height):
    pygame.font.init()
    font_big = pygame.font.SysFont("Arial", 64)
    font_small = pygame.font.SysFont("Arial", 28)

    text_game_over = font_big.render("Game Over", True, (255, 50, 50))
    text_restart = font_small.render("Press any key to restart", True, (255, 255, 255))

    screen.fill((0, 0, 0))
    screen.blit(text_game_over, ((width - text_game_over.get_width()) // 2, height // 3))
    screen.blit(text_restart, ((width - text_restart.get_width()) // 2, height // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False
