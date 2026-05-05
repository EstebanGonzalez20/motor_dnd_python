from game.actions import Action

def parse_command(text: str):
    parts = text.split()

    if parts[0] == "move":
        return Action(
            type="move",
            target_position=(parts[1], parts[2])
        )

    elif parts[0] == "attack":
        return Action(
            type="attack",
            target_position=(parts[1], parts[2])
        )
    
    elif parts[0] == "info":
        return Action(
            type="info",
            target_position=(parts[1], parts[2])
        )