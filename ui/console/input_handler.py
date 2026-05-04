from game.actions import Action

def parse_command(text: str) -> Action:
    parts = text.split()

    if parts[0] == "move":
        return Action(
            action="move",
            tile_x=int(parts[1]),
            tile_y=int(parts[2]),
        )

    elif parts[0] == "attack":
        return Action(
            action="attack",
            tile_x=int(parts[1]),
            tile_y=int(parts[2]),
        )
    
    elif parts[0] == "info":
        return Action(
            action="info",
            tile_x=int(parts[1]),
            tile_y=int(parts[2]),
        )