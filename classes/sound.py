# sonido.py
import pygame

class SoundManager:
    def __init__(self):
        pygame.mixer.init()
        self.shoot_sound = pygame.mixer.Sound("assets/sonidos/shoot.wav")
        self.hit_sound = pygame.mixer.Sound("assets/sonidos/hit.wav")

    def play_shoot(self):
        self.shoot_sound.play()

    def play_hit(self):
        self.hit_sound.play()
