from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.cell import Cell

from abc import abstractmethod, ABC

STATE_TYPE_LAND = 'L'
STATE_TYPE_WATER = 'W'
STATE_TYPE_ROAD = 'R'
STATE_TYPE_ROAD_CONSTRUCTION = 'RC'
STATE_TYPE_ROAD_DEMOLISHED = 'RD'
STATE_TYPE_HOUSE = 'H'
STATE_TYPE_HOUSE_CONSTRUCTION = 'HC'
STATE_TYPE_HOUSE_DEMOLISHED = 'HD'

class State(ABC):
    _taxes: int = None
    type: str = None

    @property
    def context(self) -> 'Cell':
        return self._context

    @context.setter
    def context(self, context: 'Cell') -> None:
        self._context = context

    def pay_taxes(self) -> int:
        return self._taxes

    def draw(self):
        return self.type

    def is_type(self, ctype: str) -> bool:
        return ctype == self.type

    @abstractmethod
    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        pass