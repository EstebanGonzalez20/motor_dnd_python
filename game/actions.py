from dataclasses import dataclass
from typing import Optional

@dataclass
class Action:
    type: str
    entity_id: int
    target_position: Optional[tuple[int, int]] = None