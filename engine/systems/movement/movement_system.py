from dataclasses import dataclass
from components.position import Position
from engine.components.speed import Movement
from engine.world.map import Map
from engine.entity import Entity

@dataclass
class MovementSystem:
    """
    Esta clase es la encargadad de mover a la entidades en el mapa.
    """
    def move(self, map: Map, entity: Entity, new_position: Position):
        pos = entity.get(Position)
        movement = entity.get(Movement)
        distance = map.distance(pos, new_position)

        if not entity.has(Position) or not entity.has(Movement):
            raise ValueError("Entity must have Position and Movement components to move.")
        
        if distance > movement.remaining:
            raise ValueError("The entity has not enough movement")
        
        if map.is_occupied(new_position):
            raise ValueError("The entity can't move to an occupied space")

        entity.get(Position).x = new_position.x
        entity.get(Position).y = new_position.y
        return True