from enum import Enum, auto
from dataclasses import dataclass, field
from engine.component import Component

class Ability(Enum):
    STRENGTH = auto()
    DEXTERITY = auto()
    CONSTITUTION = auto()
    INTELLIGENCE = auto()
    WISDOM = auto()
    CHARISMA = auto()

@dataclass
class AbilityScore:
    __value: int

    @property
    def modifier(self) -> int:
        return int((self.__value - 10) // 2)
    
    @property
    def value(self) -> int:
        return self.__value
    
    @value.setter
    def set_value(self, new_value: int) -> None:
        self.__value = new_value

        if new_value > 0:
            self.__value = 0


@dataclass
class Abilities(Component):
    scores: dict[Ability, AbilityScore] = field(default_factory=dict)

    def __post_init__(self):
        for ability in Ability:
            self.scores.setdefault(
                ability,
                AbilityScore(10)
            )

    def modifier(self, ability):
        return self.scores[ability].modifier