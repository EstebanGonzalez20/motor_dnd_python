from engine.world.map import Map
from game.game_state import GameState
from game.game_controller import GameController
from ui.console.console_ui import ConsoleUI
from engine.components.position import Position
from game.factories.entity_factory import EntityFactory
import os

def main():
    os.system("cls")
    player = EntityFactory.create_player(1)
    goblin = EntityFactory.create_monster(2)
    game_map = Map(9, 9,{})
    game_map.add_entity(player.get(Position), player)
    game_map.add_entity(goblin.get(Position), goblin)
    state = GameState(game_map)
    state.add_entity(1, player)
    state.add_entity(2, goblin)
    controller = GameController(state)
    ui = ConsoleUI(controller)
    ui.run()

main()