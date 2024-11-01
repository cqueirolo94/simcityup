from game.states.state import State, STATE_TYPE_LAND, STATE_TYPE_WATER, STATE_TYPE_ROAD, STATE_TYPE_ROAD_CONSTRUCTION, \
    STATE_TYPE_HOUSE, STATE_TYPE_HOUSE_CONSTRUCTION


class Land(State):
    type = STATE_TYPE_LAND
    _taxes = 0

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        if to_type == STATE_TYPE_WATER:
            return STATE_TYPE_WATER
        if to_type == STATE_TYPE_ROAD:
            return STATE_TYPE_ROAD_CONSTRUCTION
        if to_type == STATE_TYPE_HOUSE and road_adj:
            return STATE_TYPE_HOUSE_CONSTRUCTION
        return STATE_TYPE_LAND
