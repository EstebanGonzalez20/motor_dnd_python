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
    entities: dict[tuple[Position], Entity]

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
    
    @property
    def entities(self):
        return self.entities

    def add_entity(self, position: Position, entity: Entity) -> None:
        """
        Agrega una entidad al mapa en un espacio vacío
        """
        position_key = tuple(position)
        if position_key not in self.entities.keys():
            self.entities[position_key] = entity

        else:
            raise ValueError("The entity must be placed in an empty space")
        
    def remove_entity(self, position: Position) -> None:
        position_key = tuple(position)
        if position_key in self.entities.keys():
            self.entities.pop(position_key)

        else:
            raise ValueError("The position specified doesn't contains an entity")