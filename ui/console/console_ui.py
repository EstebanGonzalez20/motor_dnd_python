from ui.console.render import Render
from ui.console.input_handler import parse_command
import os

class ConsoleUI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            os.system("cls")
            render = Render(self.controller.state)
            render.list_entities()
            render.render_map()
            text = input("> ")
            action = parse_command(text)

            if action:
                self.controller.handle(action)