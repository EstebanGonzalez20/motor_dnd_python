from collections import deque
from dataclasses import dataclass, field
from typing import Callable
 
from engine.entity import Entity
from engine.components.action_economy import ActionEconomy
from engine.systems.combat.initiative_system import InitiativeSystem
 
@dataclass
class TurnSystem:
    """
    Gestiona el flujo de combate turno a turno.
 
    Responsabilidades:
        - Saber quién tiene el turno actual y quién sigue.
        - Resetear los recursos de turno de la entidad activa.
        - Emitir eventos para que otros sistemas reaccionen.
    """
    _initiative_system : InitiativeSystem
    _order: deque = field(default_factory=deque)
    _round: int   = field(default=1)
    _round_starter: Entity | None = None  # quien abre cada ronda
 
    # Callbacks: otros sistemas se suscriben aquí
    _on_turn_start: list[Callable[[Entity], None]] = field(default_factory=list)
    _on_turn_end:   list[Callable[[Entity], None]] = field(default_factory=list)
    _on_round_end:  list[Callable[[int],    None]] = field(default_factory=list)
 
    # -- Constructor --------------------------------------------------

    def set_order(self) -> None:
        self._order = self._initiative_system.build_turn_order()
        self._round_starter = self.current
 
    # -- Suscripciones ------------------------------------------------
 
    def on_turn_start(self, fn: Callable[[Entity], None]) -> None:
        self._on_turn_start.append(fn)
 
    def on_turn_end(self, fn: Callable[[Entity], None]) -> None:
        self._on_turn_end.append(fn)
 
    def on_round_end(self, fn: Callable[[int], None]) -> None:
        self._on_round_end.append(fn)
 
    # -- Flujo principal ----------------------------------------------
 
    def start_turn(self) -> Entity | None:
        """
        Inicia el turno de la entidad actual:
          - Resetea su ActionEconomy (acciones, bonus, movimiento, objeto).
          - Resetea su Movement.
          - Resetea su Reaction (se acumula entre turnos, no dentro del turno).
          - Dispara los callbacks on_turn_start.
        """
        entity = self.current
        if entity is None:
            return None
 
        if entity.has(ActionEconomy):
            economy : ActionEconomy = entity.get(ActionEconomy)
            economy.reset_turn()
            economy.reset_off_turn()
 
        for fn in self._on_turn_start:
            fn(entity)
 
        return entity
 
    def end_turn(self) -> None:
        """
        Finaliza el turno actual:
          - Dispara los callbacks on_turn_end.
          - Avanza al siguiente en el orden.
          - Si se completó la ronda, incrementa el contador y dispara on_round_end.
        """
        entity = self.current
        for fn in self._on_turn_end:
            fn(entity)

        self._order.rotate(-1)

        # Nueva ronda cuando vuelve a tocarle al que abrió la ronda anterior
        if self.current is self._round_starter:
            self._round += 1
            self._round_starter = self.current  # puede cambiar si se agregaron entidades
            for fn in self._on_round_end:
                fn(self._round)
 
    # -- Entidades dinámicas ------------------------------------------
 
    def add_entity(self, entity: Entity) -> None:
        """
        Añade una entidad que entra al combate a mitad de ronda.
        """
        current = self.current
        self._initiative_system.add_entity(entity)
        self.set_order()

        while self.current is not current:
            self._order.rotate(-1)


    def remove_entity(self, entity: Entity) -> None:
        """Elimina una entidad (murió, huyó, etc.)."""
        if entity is self._round_starter:
            # El que abría la ronda murió, el siguiente toma el rol
            next_index = (list(self._order).index(entity) + 1) % len(self._order)
            self._round_starter = list(self._order)[next_index]

        try:
            self._order.remove(entity)

        except ValueError:
            pass
 
    # -- Consultas ----------------------------------------------------
 
    @property
    def current(self) -> Entity | None:
        return self._order[0] if self._order else None
 
    @property
    def next(self) -> Entity | None:
        return self._order[1] if len(self._order) > 1 else None
 
    @property
    def round(self) -> int:
        return self._round