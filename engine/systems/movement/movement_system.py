from dataclasses import dataclass
from engine.components.position import Position
from engine.components.speed import Movement
from engine.world.map import Map
from engine.entity import Entity

@dataclass
class MovementResult:
    result: bool
    result_message: str

@dataclass
class MovementSystem:
    """
    Esta clase es la encargadad de mover a la entidades en el mapa.
    """
    def move(self, map: Map, entity: Entity, new_position: Position):
        current_position = entity.get(Position)
        movement = entity.get(Movement)
        distance = map.distance(current_position, new_position)

        if not entity.has(Position) or not entity.has(Movement):
            raise ValueError("Entity must have Position and Movement components to move.")
        
        if distance > movement.remaining:
            return MovementResult(
                result=False,
                result_message="The entity has not enough speed"
            )
        
        if map.is_occupied(new_position):
            return MovementResult(
                result=False,
                result_message="The entity can't move to an occupied space"
            )

        else:
            movement.consume(distance)
            map.remove_entity(current_position)
            current_position.x = new_position.x
            current_position.y = new_position.y
            map.add_entity(current_position, entity)
            return MovementResult(
                result=True,
                result_message="The movement was successfully done"
            )