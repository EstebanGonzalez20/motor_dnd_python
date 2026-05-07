from engine.entity import Entity
from engine.components.position import Position
from engine.components.speed import Movement

class CharacterFactory:

    @staticmethod
    def create_player(entity_id: int) -> Entity:
        name = input("Ingrese nombre del personaje: ")
        player = Entity(entity_id, name)
        player.add(Movement(6))
        player.add(Position(5, 5))
        return player