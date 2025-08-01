import os
import pygame

class Plane(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        base_path = os.path.dirname(__file__)  # carpeta donde está plane.py (game\classes)
        image_path = os.path.join(base_path, "..", "assets", "images", "planes_5.png")
        image_path = os.path.abspath(image_path)  # ruta absoluta segura
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, screen):
        # Dibuja el avión en la pantalla
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        # Mueve el avión por la pantalla
        self.rect.x += dx
        self.rect.y += dy

