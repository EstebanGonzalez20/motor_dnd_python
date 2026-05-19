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
        rolls = [self.roll(), self.roll()]
        return max(rolls)

    def roll_with_disadvantage(self) -> int:
        rolls = [self.roll(), self.roll()]
        return min(rolls)

    def max_roll(self) -> int:
        return self.sides
    
@dataclass
class DiceRoll:
    """
    This class represents the dice rolling needed for something.
    Example: 2d4
    """
    dice: Dice
    number_of_dice: int = 1

    def roll(self) -> int:
        return sum(self.dice.roll() for _ in range(self.number_of_dice))
    
    def max_roll(self) -> int:
        return self.dice.max_roll() * self.number_of_dice

d4 = Dice(4)
d6 = Dice(6)
d8 = Dice(8)
d10 = Dice(10)
d12 = Dice(12)
d20 = Dice(20)
d100 = Dice(100)