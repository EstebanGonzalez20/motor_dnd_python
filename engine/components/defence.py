from engine.component import Component
from dataclasses import dataclass, field

@dataclass
class Defence(Component):
    immuneties = set[str] = field(default_factory=set)
    resistances: set[str] = field(default_factory=set)
    weaknesses: set[str] = field(default_factory=set)