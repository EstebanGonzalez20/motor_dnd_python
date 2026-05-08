from engine.entity import Entity
from engine.components.position import Position
from engine.components.speed import Movement
from engine.components.hitpoints import Health

# class CharacterFactory:

#     @staticmethod
#     def create_player(entity_id: int) -> Entity:
#         name = input("Ingrese nombre del personaje: ")
#         player = Entity(entity_id, name)
#         player.add(Movement(6))
#         player.add(Position(5, 5))
#         return player

class EntityFactory:

    @staticmethod
    def create_player(entity_id: int) -> Entity:
        name = input("Ingrese nombre del personaje: ")
        player = Entity(entity_id, name)
        player.add(Health(10, 10))
        player.add(Movement(6))
        player.add(Position(5, 5))
        return player
    
    @staticmethod
    def create_monster(entity_id: int) -> Entity:
        name = "Goblin"
        monster = Entity(entity_id, name)
        monster.add(Health(6, 6))
        monster.add(Movement(6))
        monster.add(Position(9, 9))
        return monster