from enum import Enum, auto
from dataclasses import dataclass, field
from utils.dice import Dice

class DamageType(Enum):
    SLASHING = auto()
    PIERCING = auto()
    BLUDGEONING = auto()
    FIRE = auto()
    COLD = auto()
    POISON = auto()
    ACID = auto()
    NECROTIC = auto()
    LIGHTNING = auto()
    THUNDER = auto()
    PSYCHYC = auto()
    RADIANT = auto()
    FORCE = auto()

@dataclass
class DamageRoll:
    damage_type: DamageType
    dice: Dice
    number_of_dice: int = 1

    def roll(self, critical: bool = False) -> int:
        rolls = self.number_of_dice * (2 if critical else 1)
        return sum(self.dice.roll() for _ in range(rolls))

@dataclass
class Damage:
    amounts: dict[DamageType, int] = field(default_factory=dict)

    def add(self, damage_type: DamageType, amount: int) -> None:
        self.amounts[damage_type] = self.amounts.get(damage_type, 0) + amount

    def total(self) -> int:
        return sum(self.amounts.values())