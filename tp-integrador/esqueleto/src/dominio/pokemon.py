class Pokemon:
    """Clase que representa un Pokémon dentro de la Pokédex."""

    def __init__(self, numero: int, nombre: str, tipo: str, ataque: int, velocidad: int):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.ataque = ataque
        self.velocidad = velocidad

    def __repr__(self):
        return f"#{self.numero} {self.nombre} ({self.tipo}) - Atk: {self.ataque} | Vel: {self.velocidad}"
