
import pygame
import random
import sys
from config import WIDTH, HEIGHT, FPS, BLACK
from screens.home_screen import show_start_screen
from screens.game_over_screen import show_game_over_screen
from classes.cannon import Cannon
from classes.plane import Plane
from classes.bullet import Bullet
# parte de Lara Magallanes
from logic.score import Score
from logic.levels import LevelSystem
from logic.lives import Lives 


def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
      #Creamos una fuente para mostrar texto (nivel)
    font = pygame.font.Font(None, 36)
    # Mostrar pantalla de inicio (espera tecla)
    show_start_screen(screen, WIDTH, HEIGHT)

    # Crear jugador y grupos
    player = Cannon()
    planes = pygame.sprite.Group()
    bullets = []
    nivel = LevelSystem()
    vidas = Lives()  #Creamos instancia de vidas
    running = True
    game_over = False

    while running:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullets.append(player.shoot())

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-5)
        if keys[pygame.K_RIGHT]:
            player.move(5)

        mouse_x = pygame.mouse.get_pos()[0]
        player.move_to(mouse_x)

        # Generar aviones aleatorios
        if random.randint(1, 40) == 1:
            planes.add(Plane(100, 100))  # o la posición inicial que vos quieras

        # Actualizar balas
        for bullet in bullets[:]:
            bullet.update()
            bullet.draw(screen)
            if bullet.off_screen():
                bullets.remove(bullet)

        # Actualizar aviones y verificar colisiones
        for plane in planes.sprites():
            plane.update()
            plane.draw(screen)

            if plane.rect.y > HEIGHT:
                planes.remove(plane)
                vidas.lose_life()

                # 5. Si se queda sin vidas, termina el juego
                if vidas.is_game_over():
                    running = False
                    game_over = True
            for bullet in bullets:
                if plane.rect.colliderect(bullet.rect):
                    if plane in planes:
                        planes.remove(plane)
                    if bullet in bullets:
                        bullets.remove(bullet)
                    nivel.enemy_killed()
        
        player.draw(screen)
        #Mostrar nivel en pantalla
        nivel_texto = font.render(f"Nivel: {nivel.level}", True, (255, 255, 255))
        screen.blit(nivel_texto, (10, 50))
        vidas.draw(screen)  #  Mostrar vidas en pantalla
        pygame.display.flip()
        clock.tick(FPS)

    if game_over:
        show_game_over_screen(screen, WIDTH, HEIGHT)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
