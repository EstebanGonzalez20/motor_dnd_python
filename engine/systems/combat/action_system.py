from typing import Callable, Any
from engine.entity import Entity
from engine.components.action_economy import ActionEconomy, ActionType
 
class ActionSystem:
    """
    Valida y ejecuta acciones consumiendo el ActionEconomy de la entidad.
    """
 
    @staticmethod
    def can_perform(entity: Entity, action_type: ActionType) -> bool:
        if not entity.has(ActionEconomy):
            return False
        
        return entity.get(ActionEconomy).has(action_type)
 
    @staticmethod
    def spend(entity: Entity, action_type: ActionType) -> Any:
        """
        Gasta el tipo de acción a la entidad específicada
        """
        economy : ActionEconomy = entity.get(ActionEconomy)
        economy.spend(action_type)