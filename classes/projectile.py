# disparo.py
import pygame

WHITE = (255, 255, 255)
PROJECTILE_SPEED = 10

class Projectile:
    def __init__(self, x, y):
        self.width = 4
        self.height = 10
        self.x = x
        self.y = y
        self.color = WHITE
        self.speed = PROJECTILE_SPEED
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.y -= self.speed
        self.rect.y = self.y

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)

    def is_offscreen(self):
        return self.y < 0
