from engine.systems.damage.damage import DamageType, DamageRoll, Damage
from dataclasses import dataclass, field
from enum import Flag, auto

class WeaponProperty(Flag):
    NONE = 0
    FINESSE = auto()
    LIGHT = auto()
    HEAVY = auto()
    TWO_HANDED = auto()
    VERSATILE = auto()
    THROWN = auto()
    RANGED = auto()
    LOADING = auto()
    REACH = auto()
    SPECIAL = auto()

@dataclass
class Weapon:
    name: str
    ability: str
    range: int
    dice_damage: list[DamageRoll] = field(default_factory=list)
    fixed_damage: dict[DamageType, int] = field(default_factory=dict)

    def calculate_damage(self, critical: bool = False) -> Damage:
        total_damage = Damage()

        for damage_roll in self.dice_damage:
            amount = damage_roll.roll(critical)
            total_damage.add(damage_roll.damage_type, amount)

        for damage_type, amount in self.fixed_damage.items():
            total_damage.add(damage_type, amount)

        return total_damage