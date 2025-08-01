import pygame
import os

class Cannon:
    def __init__(self):
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "..", "assets", "images", "cannon.png")
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
            self.rect = self.image.get_rect()
        except Exception as e:
            print(f"Error cargando imagen: {e}")
            self.image = pygame.Surface((40, 20))
            self.image.fill((0,255,0))
            self.rect = self.image.get_rect()

        self.rect.midbottom = (400, 590)

    def move(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))

    def move_to(self, x):
        self.rect.x = x - self.rect.width // 2
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))

    def shoot(self):
        from classes.bullet import Bullet
        return Bullet(self.rect.centerx, self.rect.top)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
