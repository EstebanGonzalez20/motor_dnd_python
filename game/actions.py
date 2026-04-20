from dataclasses import dataclass

@dataclass
class MoveAction:
    entity_id: int
    x: int
    y: int

@dataclass
class AttackAction:
    attacker_id: int
    target_id: int

@dataclass
class InfoAction:
    grid_space: int