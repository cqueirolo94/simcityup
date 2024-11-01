from game.states.land import Land
from game.states.state import State, STATE_TYPE_HOUSE_DEMOLISHED, STATE_TYPE_LAND


class HouseDemolished(State):
    type = STATE_TYPE_HOUSE_DEMOLISHED
    _taxes = 0

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        return STATE_TYPE_LAND