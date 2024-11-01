from game.states.state import State, STATE_TYPE_WATER, STATE_TYPE_LAND


class Water(State):
    type = STATE_TYPE_WATER
    _taxes = 0

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        return STATE_TYPE_LAND