from engine.systems.damage.damage import DamageType, DamageRoll, Damage
from dataclasses import dataclass, field
from enum import Enum, auto

class WeaponRange:
    pass

@dataclass
class Range(WeaponRange):
    normal_range: int
    long_range: int

@dataclass
class Melee(WeaponRange):
    range: int = 1

#------------------------------------------------------------
class AmunitionTypes(Enum):
    ARROW = auto()
    SHAVING = auto()

class WeaponProperty:
    pass

@dataclass
class Amunition(WeaponProperty):
    amunittion_type: AmunitionTypes

class Finesse(WeaponProperty):
    pass

class Heavy(WeaponProperty):
    pass

class Light(WeaponProperty):
    pass

class Loading(WeaponProperty):
    pass

@dataclass
class Thrown(WeaponProperty):
    range_attack: Range

class TwoHanded(WeaponProperty):
    pass

@dataclass
class Versatile(WeaponProperty):
    two_handed_damage: list[DamageRoll]

#-------------------------------------------------------------

class WeaponType(Enum):
    SIMPLE_MELEE = auto()
    SIMPLE_RANGED = auto()
    MARTIAL_MELEE = auto()
    MARTIAL_RANGED = auto()
    IMPROVISED = auto()

class WeaponClass(Enum):
    BATTLEAXE = auto()
    CLUB = auto()
    DAGGER = auto()
    DART = auto()
    FLAIL = auto()
    GLAIVE = auto()
    GREATAXE = auto()
    GREATCLUB = auto()
    GREATSWORD = auto()
    HALBERD = auto()
    HANDAXE = auto()
    HAND_CROSSBOW = auto()
    HEAVY_CROSSBOW = auto()
    JAVELIN = auto()
    LIGTH_CROSSBOW = auto()
    LIGTH_HAMMER = auto()
    LONGBOW = auto()
    LONGSWORD = auto()
    MACE = auto()
    MAUL = auto()
    MORNINGSTAR = auto()
    PIKE = auto()
    QUARTERSTAFF = auto()
    RAPIER = auto()
    SCIMITAR = auto()
    SHORTBOW = auto()
    SHORTSWORD = auto()
    SICKLE = auto()
    SPEAR = auto()
    TRIDENT = auto()
    WAR_PICK = auto()
    WARHAMMER = auto()
    WHIP = auto()

#-------------------------------------------------------------

@dataclass
class Weapon:
    name: str
    type: WeaponType
    weapon_class: WeaponClass
    properties: list[WeaponProperty]
    range: WeaponRange
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
    
    def get_property(self, property_type: WeaponProperty):
        for property in self.properties:
            if isinstance(property, property_type):
                return property

        return None