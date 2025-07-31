import pygame
import random

class Plane:
    def __init__(self):
        self.image = pygame.image.load("assets/plane.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 800 - self.rect.width)
        self.rect.y = -self.rect.height
        self.speed = random.randint(2, 5)

    @property
    def y(self):
        return self.rect.y

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

import pygame
import random
import os

