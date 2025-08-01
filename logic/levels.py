

class LevelSystem:
    def __init__(self):
        self.level = 1
        self.enemies_destroyed = 0

    def enemy_killed(self):
        """Aumenta el contador de enemigos destruidos y sube el nivel cada 10"""
        self.enemies_destroyed += 1

        if self.enemies_destroyed >= 10:
            self.level += 1
            self.enemies_destroyed = 0  # Reiniciar el contador para el siguiente nivel

    def reset(self):
        """Reinicia el sistema de niveles"""
        self.level = 1
        self.enemies_destroyed = 0
