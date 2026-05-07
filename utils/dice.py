from dataclasses import dataclass
import random

@dataclass
class Dice:
    """
    Esta clase representa a los dados.

    ATRIBUTOS:
        sides: La cantidad de caras del dado
    """
    sides: int

    def roll(self) -> int:
        return random.randint(1, self.sides)

    def roll_with_advantage(self) -> int:
        return max(self.roll(), self.roll())

    def roll_with_disadvantage(self) -> int:
        return min(self.roll(), self.roll())

    def max_roll(self) -> int:
        return self.sides
    
d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)