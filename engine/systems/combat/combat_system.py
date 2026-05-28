from dataclasses import dataclass
from engine.systems.combat.turn_system import TurnSystem
from engine.systems.combat.attack_system import AttackSystem
from engine.entity import Entity

@dataclass
class CombatSystem:
    turn_system : TurnSystem
    _entities: list[Entity]

    @property
    def entities(self):
        return self._entities
