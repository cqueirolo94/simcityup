from game.states.state import State, STATE_TYPE_HOUSE_CONSTRUCTION, STATE_TYPE_HOUSE, STATE_TYPE_ROAD_DEMOLISHED


class HouseConstruction(State):
    type = STATE_TYPE_HOUSE_CONSTRUCTION
    _taxes = 10

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        return STATE_TYPE_HOUSE if not event else STATE_TYPE_ROAD_DEMOLISHED