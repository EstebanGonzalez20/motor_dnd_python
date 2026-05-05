from dataclasses import dataclass
from typing import Optional

@dataclass
class Action:
    type: str
    target_position: Optional[tuple[int, int]] = None