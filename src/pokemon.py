class Pokemon:
    
    def __init__ (self, numero: int, nombre: str, tipo1: str, tipo2: str, hp: int, ataque: int, defensa: int, velocidad: int, generation: int):
        self.numero = numero
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generation = generation

    def __repr__(self):
        return f"#{self.numero} {self.nombre} ({self.tipo1}) - HP: {self.hp} | Atk: {self.ataque} | Def: {self.defensa} | Vel: {self.velocidad}"