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
        roll : int = d20.roll()
        result : int = roll + abilities.modifier(Ability.STRENGTH)
        armorclass : ArmorClass = target.get(ArmorClass)

        return AttackResult(
            hit = result >= armorclass.value ,
            crit = roll == 20
        )