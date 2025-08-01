import pygame
import random
from config import WIDTH, HEIGHT, FPS, BLACK
from classes.cannon import Cannon
from classes.plane import Plane
from classes.bullet import Bullet
import sys
# pantalla de inicio
def show_start_screen(screen, width, height):
    pygame.init()
    
    font = pygame.font.SysFont("Arial", 48)
    title_text = font.render("Anti-Aircraft", True, (255, 255, 255))
    press_key_text = pygame.font.SysFont("Arial", 24).render("Presiona para empezar", True, (255, 255, 255))
    
    screen.fill((0, 0, 0))
    screen.blit(title_text, ((width - title_text.get_width()) // 2, height // 3))
    screen.blit(press_key_text, ((width - press_key_text.get_width()) // 2, height // 2))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

show_start_screen(screen, WIDTH, HEIGHT) #mostrar pantalla de incio

# Crear jugador y listas
player = Cannon()  # Crea el cañón del jugador
planes = []  # Lista que guarda los aviones enemigos
bullets = []  # Lista que guarda las balas disparadas
planes = pygame.sprite.Group()
planes.add(Plane(100, -50)) 
running = True  # Variable para controlar si el juego sigue en ejecución

# Loop principal
while running:
    screen.fill(BLACK)  # Pinta el fondo negro en cada frame

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Si el jugador cierra la ventana
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # Si se presiona espacio, dispara
                bullets.append(player.shoot())

    # Movimiento del jugador con flechas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-5)  # Mueve a la izquierda
    if keys[pygame.K_RIGHT]:
        player.move(5)  # Mueve a la derecha
        
    # Movimiento del jugador con mouse (opcional)
    mouse_x = pygame.mouse.get_pos()[0]  # Solo toma la posición x
    player.move_to(mouse_x)  # Se mueve directo al mouse (opcional)


    # Crear aviones aleatorios cada ciertos frames
    if random.randint(1, 40) == 1:
        planes.append(Plane())

    # Actualizar y dibujar balas
    for bullet in bullets[:]:
        bullet.update()  # Mueve la bala
        bullet.draw(screen)  # La dibuja
        if bullet.off_screen():
            bullets.remove(bullet)  # Elimina si sale de la pantalla

    # Actualizar y dibujar aviones
    for plane in planes[:]:
        plane.update()  # Baja el avion
        plane.draw(screen)  # Lo dibuja
        if plane.y > HEIGHT:  # Si el avion llega al suelo
            running = False  # Perdes
        for bullet in bullets:
            if plane.rect.colliderect(bullet.rect):  # Si colisiona con bala
                if plane in planes:
                    planes.remove(plane)
                if bullet in bullets:
                    bullets.remove(bullet)

    # Dibujar jugador (el cañón)
    player.draw(screen)

    pygame.display.flip()  # Actualiza la pantalla
    clock.tick(FPS)  # Controla los FPS

pygame.quit()  # Cierra el juego
