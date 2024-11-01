from game.states.state import State, STATE_TYPE_HOUSE, STATE_TYPE_HOUSE_DEMOLISHED


class House(State):
    type = STATE_TYPE_HOUSE
    _taxes = 20

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        return STATE_TYPE_HOUSE_DEMOLISHED