from engine.components.position import Position
from engine.components.hitpoints import Health
from engine.world.map import Map

print(str([1, 1]))

def render_map(map: Map):
    print("\n=== ENTIDADES ===")

    for position, entity in map.entities:
        hp = entity.get(Health)
        position = entity.get(Position)
        print(f"Position: {position.x} {position.y}, Entity: {entity.name}, HP: {hp}")
    
    width = ""
    for i in range(map.width):
        width += i
