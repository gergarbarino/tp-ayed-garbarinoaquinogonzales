class Pokemon:
    """Clase que representa un Pokémon dentro de la Pokédex."""

    def __init__(self, numero: int, nombre: str, tipo: str, hp: int, ataque: int, defensa: int, velocidad: int):
        self.numero = numero
        self.nombre = nombre
        self.tipo = tipo
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad

    def __repr__(self):
        return f"#{self.numero} {self.nombre} ({self.tipo}) - HP: {self.hp} | Atk: {self.ataque} | Def: {self.defensa} | Vel: {self.velocidad}"
