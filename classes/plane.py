import pygame
import random
import os

class Plane(pygame.sprite.Sprite):
    def __init__(self, x=None, y=None):
        super().__init__()
        current_path = os.path.dirname(__file__)
        image_path = os.path.join(current_path, "..", "assets", "images", "plane.png")
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except Exception as e:
            print(f"Error cargando plane.png: {e}")
            self.image = pygame.Surface((60, 30))
            self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        
        if x is None:
            self.rect.x = random.randint(0, 800 - self.rect.width)
        else:
            self.rect.x = x
            
        if y is None:
            self.rect.y = -self.rect.height
        else:
            self.rect.y = y
            
        self.speed = random.randint(2, 5)

    @property
    def y(self):
        return self.rect.y

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)
