from dataclasses import dataclass
from engine.component import Component

@dataclass
class ArmorClass(Component):
    """
    Esta clase representa la clase de armadura que tiene la entidad
    """
    def __init__(self, value: int):
        self._value = value if value >= 0 else 0

    @property
    def value(self) -> int:
        return self._value

    @value.setter
    def value(self, new_value: int) -> None:
        self.value = new_value if new_value >= 0 else 0