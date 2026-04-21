from dataclasses import dataclass
from engine.components.position import Position
from engine.entity import Entity

@dataclass
class Map:
    """
    Esta clase representa a un tablero
    """
    width: int
    height: int
    entities: dict[Position, Entity]

    def distance(self, pos1: Position, pos2: Position) -> int:
        """
        Calcula la distancia entre dos posiciones del mapa
        """
        return abs(pos1.x - pos2.x) + abs(pos1.y - pos2.y)
    
    def is_occupied(self, position: tuple) -> bool:
        """
        Consulta si una posición del mapa esta ocupada
        """
        return position in self.entities