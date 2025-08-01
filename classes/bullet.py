import pygame
import os

class Bullet:
    def __init__(self, x, y):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "..", "assets", "images", "bullet.png")
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except Exception as e:
            print(f"Error cargando bullet.png: {e}")
            self.image = pygame.Surface((5, 10))
            self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -7

    def update(self):
        self.rect.y += self.speed

    def off_screen(self):
        return self.rect.bottom < 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
