from engine.component import Component
from engine.models.weapon import Weapon
from dataclasses import dataclass

@dataclass
class HandWielding(Component):
    _right_hand : Weapon = None
    _left_hand: Weapon = None

    @property
    def free_hand(self):
        if not self._right_hand:
            return self._right_hand
        
        elif not self._left_hand:
            return self._left_hand
        
        else:
            return None


    def equip(self, weapon: Weapon, hand : str = None):
        if hand:
            match hand:
                case "right":
                    self._right_hand = weapon

                case "left":
                    self._left_hand = weapon

        else:
            self.free_hand = weapon