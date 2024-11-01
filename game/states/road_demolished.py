from game.states.state import State, STATE_TYPE_ROAD_DEMOLISHED, STATE_TYPE_LAND


class RoadDemolished(State):
    type = STATE_TYPE_ROAD_DEMOLISHED
    _taxes = 0

    def next_state(self, event: bool, to_type: str, road_adj: bool) -> str:
        return STATE_TYPE_LAND