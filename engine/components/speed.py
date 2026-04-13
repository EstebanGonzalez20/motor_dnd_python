from engine.component import Component
from dataclasses import dataclass, field

@dataclass
class Movement(Component):
    """
    Esta clase permite a una entidad moverse,
    además almacena las velocidades.
    """
    _speed: int
    remaining: int = field(init=False)

    def __post_init__(self):
        self.remaining = self.speed

    def reset(self) -> None:
        """
        Este método reinicia el valor de remaining.
        """
        self.remaining = self.speed

    def consume(self, amount: int) -> None:
        """
        Este método consume movimiento.
        """
        if amount > self.remaining:
            raise ValueError("Not enough movement")

        self.remaining -= amount

    @property
    def speed(self) -> int:
        return self._speed
    
    @speed.setter
    def speed(self, value: int) -> None:
        self._speed = value