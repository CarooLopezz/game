# jugador.py
import pygame
from disparo import Projectile

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CANNON_SPEED = 5
BLUE = (0, 0, 255)

class PlayerCannon:
    def __init__(self):
        self.width = 50
        self.height = 30
        self.x = (SCREEN_WIDTH - self.width) // 2
        self.y = SCREEN_HEIGHT - self.height - 10
        self.color = BLUE
        self.speed = CANNON_SPEED

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.width, self.height))

    def shoot(self):
        return Projectile(self.x + self.width // 2 - 2, self.y)
