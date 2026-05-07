from engine.systems.movement.movement_system import MovementSystem
#from engine.systems.combat_system import CombatSystem
from engine.components.position import Position

from .actions import Action
from .game_state import GameState


class GameController:
    def __init__(self, state: GameState):
        self.state = state
        self.movement_system = MovementSystem()
        #self.combat_system = CombatSystem()

    # Punto único de entrada desde la UI
    def handle(self, action: Action):
        if action.type == "move":
            self._handle_move(action)

        # elif isinstance(action, AttackAction):
        #     self._handle_attack(action)

    # -----------------------------

    def _handle_move(self, action: Action):
        entity = self.state.get_entity(action.entity_id)
        new_position = action.target_position

        moved = self.movement_system.move(
            self.state.game_map,
            entity,
            Position(int(new_position[0]), int(new_position[1]))
        )

        print(moved.result_message)
        input("Press enter to continue... ")
    # -----------------------------

    # def _handle_attack(self, action: AttackAction):

    #     attacker = self.state.get_entity(action.attacker_id)
    #     target = self.state.get_entity(action.target_id)

    #     self.combat_system.attack(attacker, target, self.state.game_map)