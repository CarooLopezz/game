

import pygame

class Lives:
    def __init__(self, total=3, font_size=30, font_color=(255, 0, 0)):
        """
        Clase para manejar las vidas del jugador.

        :param total: Cantidad inicial de vidas.
        :param font_size: Tamaño del texto que muestra las vidas.
        :param font_color: Color del texto de vidas.
        """
        self.total = total
        self.font = pygame.font.Font(None, font_size)
        self.color = font_color
        self.position = (10, 70)  # Posición en pantalla

    def lose_life(self):
        """
        Resta una vida.
        """
        if self.total > 0:
            self.total -= 1

    def is_game_over(self):
        """
        Verifica si el jugador se quedó sin vidas.

        :return: True si no quedan vidas.
        """
        return self.total <= 0

    def draw(self, screen):
        """
        Dibuja las vidas en pantalla.

        :param screen: Superficie principal del juego.
        """
        lives_text = self.font.render(f"Lives: {self.total}", True, self.color)
        screen.blit(lives_text, self.position)

    def reset(self):
        """
        Reinicia las vidas (opcional).
        """
        self.total = 3
