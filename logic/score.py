# Clase que maneja el puntaje del jugador

class Score:
    def _init_(self):
        # El puntaje comienza en 0
        self.current_score = 0

    def increase(self, amount=1):
        """
        Aumenta el puntaje actual.
        Parámetro amount: cuánto se suma (por defecto, 1)
        """
        self.current_score += amount

    def reset(self):
        """
        Reinicia el puntaje a 0 (por ejemplo, al comenzar una nueva partida)
        """
        self.current_score = 0

    def get_score(self):
        """
        Devuelve el puntaje actual
        """
        return self.current_score