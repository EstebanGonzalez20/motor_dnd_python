from dataclasses import dataclass
from engine.entity import Entity
from engine.models.weapon import Weapon
from engine.components.abilities import Ability, Abilities
from engine.components.armorclass import ArmorClass
from utils.dice import d20

@dataclass
class AttackResult:
    crit : bool
    hit: bool

class AttackSystem:

    @staticmethod
    def attack_roll(attacker: Entity, target: Entity) -> AttackResult:
        abilities: Abilities = attacker.get(Abilities)
        roll = d20.roll() + abilities.modifier(Ability.STRENGTH)

        return AttackResult(
            hit= roll >= target.get(ArmorClass).value,
            crit= roll == 20
        )

