from dataclasses import dataclass
 
from engine.entity import Entity
from engine.components.action_economy import ActionType
from engine.components.hitpoints import Health
from engine.systems.combat.turn_system import TurnSystem
from engine.systems.combat.action_system import ActionSystem
from engine.systems.combat.attack_system import AttackSystem, AttackResult
from engine.systems.damage.damage_system import DamageSystem
from engine.systems.combat.initiative_system import InitiativeSystem
 
@dataclass
class CombatResult:
    success: bool
    message: str
  
@dataclass
class CombatSystem:
    """
    Orquesta el flujo de combate: valida turnos, cobra acciones
    y delega la ejecución a los sistemas específicos.
    No contiene lógica de ataque ni daño, solo coordinación.
    """
    _turn_system:   TurnSystem
    _damage_system: DamageSystem
 
    # -- Setup --------------------------------------------------------
 
    @classmethod
    def start(cls, initiative_system: InitiativeSystem) -> "CombatSystem":
        """Arranca el combate a partir del orden de iniciativa."""
        turn_system = TurnSystem.from_initiative(initiative_system)
        instance = cls(
            _turn_system=turn_system,
            _attack_system=AttackSystem(),
            _damage_system=DamageSystem(),
        )
        turn_system.start_turn()
        return instance
 
    # -- Consultas ----------------------------------------------------
 
    @property
    def current_entity(self) -> Entity | None:
        return self._turn_system.current
 
    @property
    def round(self) -> int:
        return self._turn_system.round
 
    def is_turn_of(self, entity: Entity) -> bool:
        return self._turn_system.current is entity
 
    # -- Acciones de combate ------------------------------------------
 
    def attack(self, attacker: Entity, target: Entity, damage_roll) -> CombatResult:
        """
        Ejecuta un ataque cuerpo a cuerpo estándar:
          1. Valida que sea el turno del atacante.
          2. Cobra la ACTION del atacante.
          3. Delega la tirada de ataque a AttackSystem.
          4. Si impacta, delega el daño a DamageSystem.
          5. Si el target muere, lo elimina del combate.
        """
        if not self.is_turn_of(attacker):
            return CombatResult(False, f"No es el turno de {attacker.name}")
 
        if not ActionSystem.can_perform(attacker, ActionType.ACTION):
            return CombatResult(False, f"{attacker.name} no tiene acciones disponibles")
 
        if not target.has(Health) or not target.get(Health).alive:
            return CombatResult(False, f"{target.name} ya está fuera de combate")
 
        ActionSystem.spend(attacker, ActionType.ACTION)
 
        result: AttackResult = ActionSystem.attack_roll(attacker, target)
 
        if not result.hit:
            return CombatResult(True, f"{attacker.name} ataca a {target.name}: falla")
 
        damage = damage_roll.critical_roll() if result.crit else damage_roll.roll()
        damage_done = self._damage_system.apply_damage(target, damage)
 
        # Eliminar del combate si murió
        if not target.get(Health).alive:
            self._turn_system.remove_entity(target)
            return CombatResult(
                True,
                f"{'¡Crítico! ' if result.crit else ''}"
                f"{attacker.name} ataca a {target.name}: "
                f"{damage_done.total()} de daño. {target.name} cae."
            )
 
        return CombatResult(
            True,
            f"{'¡Crítico! ' if result.crit else ''}"
            f"{attacker.name} ataca a {target.name}: {damage_done.total()} de daño."
        )
 
    # -- Flujo de turno -----------------------------------------------
 
    def end_turn(self, entity: Entity) -> CombatResult:
        """El GameController llama a esto cuando el jugador/IA termina su turno."""
        if not self.is_turn_of(entity):
            return CombatResult(False, f"No es el turno de {entity.name}")
 
        self._turn_system.end_turn()
        self._turn_system.start_turn()
        return CombatResult(True, f"Turno de {self._turn_system.current.name}")
 
    def add_entity(self, entity: Entity) -> None:
        """Añade una entidad al combate en curso."""
        self._turn_system.add_entity(entity)
 
    def remove_entity(self, entity: Entity) -> None:
        """Elimina una entidad del combate (huyó, murió por efecto, etc.)."""
        self._turn_system.remove_entity(entity)
 
    # -- Estado del combate -------------------------------------------
 
    @property
    def is_over(self) -> bool:
        """
        El combate termina cuando solo quedan entidades del mismo bando.
        Por ahora chequea si quedó una sola entidad viva.
        Expandir cuando tengas un componente de facción/bando.
        """
        return len(self._turn_system._order) <= 1
