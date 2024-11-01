from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game import Board
from game.states.house import House
from game.states.house_construction import HouseConstruction
from game.states.house_demolished import HouseDemolished
from game.states.land import Land
from game.states.road import Road
from game.states.road_construction import RoadConstruction
from game.states.road_demolished import RoadDemolished
from game.states.state import STATE_TYPE_WATER, STATE_TYPE_LAND, STATE_TYPE_ROAD, STATE_TYPE_ROAD_CONSTRUCTION, \
    STATE_TYPE_ROAD_DEMOLISHED, STATE_TYPE_HOUSE, STATE_TYPE_HOUSE_CONSTRUCTION, STATE_TYPE_HOUSE_DEMOLISHED
from game.states.water import Water


class Cell:
    _state = Water()

    def __init__(self, board: 'Board', row: int, col: int):
        self._row = row
        self._col = col
        self._board = board

    def transition_to(self, event: bool, to_type: str):
        road_adj = self._board.is_cell_adjacent_to_road(self._row, self._col)
        next_state = self._state.next_state(event, to_type, road_adj)

        if next_state == STATE_TYPE_WATER:
            self._state = Water()
        if next_state == STATE_TYPE_LAND:
            self._state = Land()
        if next_state == STATE_TYPE_ROAD:
            self._state = Road()
        if next_state == STATE_TYPE_ROAD_CONSTRUCTION:
            self._state = RoadConstruction()
        if next_state == STATE_TYPE_ROAD_DEMOLISHED:
            self._state = RoadDemolished()
        if next_state == STATE_TYPE_HOUSE:
            self._state = House()
        if next_state == STATE_TYPE_HOUSE_CONSTRUCTION:
            self._state = HouseConstruction()
        if next_state == STATE_TYPE_HOUSE_DEMOLISHED:
            self._state = HouseDemolished()

        self._state.context = self

    def pay_taxes(self)->int:
        return self._state.pay_taxes()

    def draw(self) -> str:
        return self._state.draw()

    def is_type(self, ctype: str) -> bool:
        return self._state.is_type(ctype)

    def advance_time(self, time: int):
        pass