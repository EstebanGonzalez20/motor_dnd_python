from enum import Enum, auto
from dataclasses import dataclass, field
from utils.dice import Dice, DiceRoll

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
class DamageRoll(DiceRoll):
    damage_type: DamageType
    
    def critical_roll(self, max: bool = False) -> int:
        if max:
            return self.dice.max_roll() + self.number_of_dice * 2
        
        else:
            rolls = self.number_of_dice * 2
            return sum(self.dice.roll() for _ in range(rolls))

@dataclass
class Damage:
    amounts: dict[DamageType, int] = field(default_factory=dict)

    def add(self, damage_type: DamageType, amount: int) -> None:
        self.amounts[damage_type] = self.amounts.get(damage_type, 0) + amount

    def total(self) -> int:
        return sum(self.amounts.values())