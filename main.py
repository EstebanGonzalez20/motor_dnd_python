from engine.world.map import Map
from game.game_state import GameState
from game.game_controller import GameController
from ui.console.console_ui import ConsoleUI
from engine.entity import Entity
from engine.components.position import Position
from engine.components.speed import Movement
import os

def crear_personaje() -> Entity:
    os.system("cls")
    name = input("Ingrese el nombre de jugador: ")
    player = Entity(1, name)
    player.add(Movement(6))
    player.add(Position(5, 5))
    return player

def main():
    player = crear_personaje()
    game_map = Map(9, 9,{})
    game_map.add_entity(player.get(Position), player)
    state = GameState(game_map)
    state.add_entity(1, player)
    controller = GameController(state)
    ui = ConsoleUI(controller)
    ui.run()

main()