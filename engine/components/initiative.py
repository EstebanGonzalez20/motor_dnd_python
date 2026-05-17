from dataclasses import dataclass
from engine.component import Component

@dataclass
class Initiative(Component):
    bonus: int = 0