from collections import deque
from dataclasses import dataclass, field
from engine.components.initiative import Initiative
from engine.components.abilities import Abilities, Ability
from engine.entity import Entity
from utils.dice import d20

@dataclass
class InitiativeSystem:
    # Lista paralela de (score, entity) ordenada descendente
    _entries: list = field(default_factory=list)

    @staticmethod
    def _roll(entity: Entity) -> int:
        return (
            d20.roll() + entity.get(Initiative).bonus + entity.get(Abilities).modifier(Ability.DEXTERITY)
        )

    def add_entity(self, entity: Entity) -> None:
        for comp in (Initiative, Abilities):
            if not entity.has(comp):
                raise ValueError(f"Entity must have {comp.__name__}")

        score = self._roll(entity)
        # Inserción binaria: negamos score para mantener orden descendente
        import bisect
        bisect.insort(self._entries, (-score, entity.id, entity))

    def remove_entity(self, entity: Entity) -> None:
        self._entries = [e for e in self._entries if e[2] is not entity]

    def build_turn_order(self) -> deque:
        """Produce el deque listo para TurnSystem."""
        return deque(entity for (_, __, entity) in self._entries)