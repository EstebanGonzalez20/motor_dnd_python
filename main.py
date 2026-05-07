from engine.world.map import Map
from game.game_state import GameState
from game.game_controller import GameController
from ui.console.console_ui import ConsoleUI
from engine.components.position import Position
from game.factories.character_factory import CharacterFactory
import os

def main():
    os.system("cls")
    player = CharacterFactory.create_player(1)
    game_map = Map(9, 9,{})
    game_map.add_entity(player.get(Position), player)
    state = GameState(game_map)
    state.add_entity(1, player)
    controller = GameController(state)
    ui = ConsoleUI(controller)
    ui.run()

main()