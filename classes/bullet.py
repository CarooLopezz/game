import pygame

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = -7

    def update(self):
        self.rect.y += self.speed

    def off_screen(self):
        return self.rect.bottom < 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)
