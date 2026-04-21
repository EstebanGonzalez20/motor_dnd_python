from engine.components.position import Position
from engine.components.hitpoints import Health
from engine.world.map import Map

print(str([1, 1]))

def render_map(map: Map):
    print("\n=== ENTIDADES ===")

    for position, entity in map.entities.items():
        hp = entity.get(Health)
        print(f"Position: {position[0]} {position[1]}, Entity: {entity.name}, HP: {hp}")
    
    width = "  "
    for i in range(1, map.width + 1):
        width += str(i) + " "

    print(width)
    for row in range(1, map.height + 1):
        actual_row = str(row) + " "
        for column in range(1, map.width + 1):
            if map.is_occupied((column, row)):
                actual_row += "© "

            else:
                actual_row += "■ "
        
        print(actual_row)

