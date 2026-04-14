from dataclasses import dataclass, field
from typing import Dict

from engine.entity import Entity
from engine.world.map import Map


@dataclass
class GameState:
    """
    Esta clase representa el estado del juego
    """
    game_map: Map
    entities: Dict[int, Entity] = field(default_factory=dict)

    def add_entity(self, entity_id: int, entity: Entity) -> None:
        self.entities[entity_id] = entity

    def get_entity(self, entity_id: int) -> Entity:
        return self.entities[entity_id]

    def all_entities(self) -> list[Entity]:
        return self.entities.values()