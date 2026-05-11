from engine.entity import Entity
from engine.components.defence import Defence
from engine.components.hitpoints import Health
from engine.systems.damage.damage import Damage, DamageType

class DamageSystem:
    @staticmethod
    def apply_damage(entity: Entity, damage: Damage) -> Damage:
        total_damage = 0
        damage_done = Damage()

        if not entity.has(Health):
            raise ValueError("The entity must have a Health component")
        
        if not entity.has(Defence):
            raise ValueError("The entity musy have a Defence component")
    
        entity_defences = entity.get(Defence)
        for damageType, damage in damage.amounts.items():
            if damageType in entity_defences.immunities:
                damage_done.add(damageType, 0)

            elif damageType in entity_defences.resistances:
                final_damage = round(damage * 0.5)
                damage_done.add(damageType, final_damage)
                total_damage += final_damage

            elif damageType in entity_defences.weaknesses:
                final_damage = damage * 2
                damage_done.add(damageType, final_damage)
                total_damage += final_damage

            else:
                damage_done.add(damageType, damage)
                total_damage += damage

        entity.get(Health).take_damage(total_damage)
        return damage_done