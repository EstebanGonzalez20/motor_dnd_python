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
    def perform(entity: Entity, action_type: ActionType, action_fn: Callable[..., Any], *args, **kwargs,) -> Any:
        """
        Gasta la acción y ejecuta action_fn si hay recursos disponibles.
        Lanza ValueError si la entidad no tiene la acción disponible.
        """
        economy = entity.get(ActionEconomy)
        
        if economy is None:
            raise ValueError(f"'{entity.name}' doesn't have an ActionEconomy component")
 
        if not economy.spend(action_type):
            raise ValueError(
                f"'{entity.name}' no tiene {action_type} disponible "
                f"(restantes: {economy.remaining(action_type)})"
            )
 
        return action_fn(*args, **kwargs)