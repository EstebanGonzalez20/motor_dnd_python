from ui.console.render import render
from ui.console.input_handler import parse_command

class ConsoleUI:
    def __init__(self, controller):
        self.controller = controller

    def run(self):
        while True:
            render(self.controller.state)
            text = input("> ")
            action = parse_command(text)

            if action:
                self.controller.handle(action)