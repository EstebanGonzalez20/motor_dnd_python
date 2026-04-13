from dataclasses import dataclass
from engine.component import Component

@dataclass
class Health(Component):
    __hp: int
    __max_hp: int

    @property
    def hp(self) -> int:
        return self.__hp
    
    @hp.setter
    def hp(self, value: int):
        self.__hp = max(0, min(value, self.__max_hp))

    @property
    def max_hp(self) -> int:
        return self.__max_hp
    
    @max_hp.setter
    def max_hp(self, value: int):
        self.__max_hp = max(1, value)
        if self.__hp > self.__max_hp:
            self.__hp = self.__max_hp

    def take_damage(self, amount: int):
        self.hp -= amount

    def heal(self, amount: int):
        self.hp += amount

    @property
    def alive(self):
        return self.hp > 0