from engine.components.position import Position
from engine.components.hitpoints import Health
from game.game_state import GameState
from engine.world.map import Map

class Render:
    def __init__(self, state: GameState):
        self.state = state

    def list_entities(self):
        entities = self.state.all_entities()
        print("\n=== ENTIDADES ===")

        for entity in entities:
            position = entity.get(Position)
            print(f"Position: x: {position.x} y: {position.y} , Entity: {entity.name}")

    def render_map(self):
        width = "  "
        for i in range(1, self.state.game_map.width + 1):
            width += str(i) + " "

        print(width)
        for row in range(1, self.state.game_map.height + 1):
            actual_row = str(row) + " "
            for column in range(1, self.state.game_map.width + 1):
                if self.state.game_map.is_occupied((column, row)):
                    actual_row += "© "

                else:
                    actual_row += "■ "
            
            print(actual_row)