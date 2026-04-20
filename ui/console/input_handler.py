from game.actions import MoveAction, AttackAction, InfoAction

def parse_command(text: str):
    parts = text.split()

    if parts[0] == "move":
        return MoveAction(
            entity_id=int(parts[1]),
            x=int(parts[2]),
            y=int(parts[3]),
        )

    elif parts[0] == "attack":
        return AttackAction(
            attacker_id=int(parts[1]),
            target_id=int(parts[2]),
        )