from game.states.state import State, STATE_TYPE_ROAD_CONSTRUCTION, STATE_TYPE_ROAD, STATE_TYPE_ROAD_DEMOLISHED


class RoadConstruction(State):
    type = STATE_TYPE_ROAD_CONSTRUCTION
    _taxes = 0

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        return STATE_TYPE_ROAD if not event else STATE_TYPE_ROAD_DEMOLISHED