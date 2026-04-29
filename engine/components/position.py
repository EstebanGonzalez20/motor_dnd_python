from engine.component import Component
from dataclasses import dataclass

@dataclass
class Position(Component):
    """
    Esta clase permite le da una ubicación a la entidad
    dentro de un mapa.
    """
    _x: int
    _y: int

    @property
    def x(self) -> int:
        return self._x
    
    @x.setter
    def x(self, value: int):
        self._x = value

    @property
    def y(self) -> int:
        return self._y
    
    @y.setter
    def y(self, value: int):
        self._y = value

    @property
    def tuple_position(self) -> tuple[int, int]:
        return (self.x, self.y)