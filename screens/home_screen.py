import pygame
import sys

def show_start_screen(screen, width, height):
    pygame.init()
    
    # Cargar fuente e imagen
    font = pygame.font.SysFont("Arial", 48)
    title_text = font.render("Anti-Aircraft", True, (255, 255, 255))
    press_key_text = pygame.font.SysFont("Arial", 24).render("Press any key to start", True, (255, 255, 255))
    
    # Fondo negro 
    screen.fill((0, 0, 0))
    
    # Centrado
    screen.blit(title_text, ((width - title_text.get_width()) // 2, height // 3))
    screen.blit(press_key_text, ((width - press_key_text.get_width()) // 2, height // 2))

    pygame.display.flip()

    # Esperar que el jugador presione algo
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False