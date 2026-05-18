from dataclasses import dataclass, field
from enum import auto, StrEnum
from engine.component import Component
 
class ActionType(StrEnum):
    ACTION = auto()
    BONUS_ACTION = auto()
    REACTION = auto()
    MOVEMENT = auto()
    OBJECT = auto()
    MAGIC = auto()
    LEGENDARY = auto()
    LAIR = auto()
 
@dataclass
class ActionPool:
    """Cantidad disponible de un tipo de acción."""
    max: int
    resets_on_turn: bool = True
    current: int = field(init=False)
 
    def __post_init__(self):
        self.current = self.max
 
    def spend(self, amount: int = 1) -> None:
        if self.current < amount:
            raise ValueError("The amount value can't be greater than the current value")
        
        self.current -= amount
 
    def reset(self) -> None:
        self.current = self.max
 
    @property
    def exhausted(self) -> bool:
        return self.current <= 0
 
 
@dataclass
class ActionEconomy(Component):
    _pools: dict[ActionType, ActionPool] = field(default_factory=dict)
 
    # -- Constructor --------------------------------------------------
 
    @staticmethod
    def create(
        actions: int = 1,
        bonus_actions: int = 1,
        reactions: int = 1,
        movement: int = 1,
        object_interactions: int = 1,
    ) -> "ActionEconomy":
        economy = ActionEconomy()
        economy.grant(ActionType.ACTION, actions)
        economy.grant(ActionType.BONUS_ACTION, bonus_actions)
        economy.grant(ActionType.REACTION, reactions)
        economy.grant(ActionType.MOVEMENT, movement)
        economy.grant(ActionType.OBJECT, object_interactions)
        return economy
 
    # -- Setup --------------------------------------------------------
 
    def grant(self, action_type: ActionType, amount: int = 1, resets_on_turn: bool = True) -> None:
        """Agrega o incrementa un pool de acciones."""
        if action_type in self._pools:
            self._pools[action_type].max     += amount
            self._pools[action_type].current += amount

        else:
            self._pools[action_type] = ActionPool(
                max=amount,
                resets_on_turn=resets_on_turn
            )
 
    def revoke(self, action_type: ActionType, amount: int = 1) -> None:
        """Quita acciones (ej: condición 'aturdido' quita ACTION)."""
        pool = self._pools.get(action_type)
        if pool is None:
            return
        pool.max     = max(0, pool.max - amount)
        pool.current = min(pool.current, pool.max)
        if pool.max == 0:
            del self._pools[action_type]
 
    # -- Consultas ----------------------------------------------------
 
    def has(self, action_type: ActionType, amount: int = 1) -> bool:
        pool = self._pools.get(action_type)
        return pool is not None and pool.current >= amount
 
    def remaining(self, action_type: ActionType) -> int:
        pool = self._pools.get(action_type)
        return pool.current if pool else 0
 
    # -- Consumo ------------------------------------------------------
 
    def spend(self, action_type: ActionType, amount: int = 1) -> bool:
        pool = self._pools.get(action_type)
        if pool is None:
            raise ValueError(f"The entity doesn't have {action_type} action")
        
        return pool.spend(amount)
 
    # -- Reset --------------------------------------------------------
 
    def reset_turn(self) -> None:
        """Resetea todo lo que se renueva al inicio del turno."""
        for pool in self._pools.values():
            if pool.resets_on_turn:
                pool.reset()
 
    def reset_off_turn(self) -> None:
        """Resetea lo que se renueva entre turnos (legendarias)."""
        for pool in self._pools.values():
            if not pool.resets_on_turn:
                pool.reset()