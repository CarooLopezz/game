import pygame

class Cannon:
    def __init__(self):
        self.image = pygame.image.load("assets/cannon.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = (400, 590)

    def move(self, dx):
        self.rect.x += dx
        self.rect.x = max(0, min(800 - self.rect.width, self.rect.x))

    def shoot(self):
        from classes.bullet import Bullet
        return Bullet(self.rect.centerx, self.rect.top)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
