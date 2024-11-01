from game.cell import Cell
from game.states.state import STATE_TYPE_ROAD


class Board:
    def __init__(self, rows: int, cols: int):
        self._rows: int = rows
        self._cols: int = cols
        self._board: list[list[Cell]] = []

        for row in range(self._rows):
            self._board.append([])
            for col in range(self._cols):
                self._board[row].append(Cell(self, col, row))

    def draw(self) -> list[str]:
        representation = []
        for row in self._board:
            for cell in row:
                representation.append(cell.draw())
            representation.append('\n')

        return representation

    def is_cell_adjacent_to_road(self, row: int, col: int):
        if row == 0:
            if col == 0:
                return (self._board[row][col+1].is_type(STATE_TYPE_ROAD)
                        or self._board[row+2][col].is_type(STATE_TYPE_ROAD))
            if col == self._cols-1:
                return (self._board[row][col-1].is_type(STATE_TYPE_ROAD)
                        or self._board[row+1][col].is_type(STATE_TYPE_ROAD))
            return (self._board[row][col - 1].is_type(STATE_TYPE_ROAD)
                    or self._board[row][col + 1].is_type(STATE_TYPE_ROAD)
                    or self._board[row + 1][col].is_type(STATE_TYPE_ROAD))

        if row == self._rows-1:
            if col == 0:
                return (self._board[row][col+1].is_type(STATE_TYPE_ROAD)
                        or self._board[row-1][col].is_type(STATE_TYPE_ROAD))
            if col == self._cols-1:
                return (self._board[row][col-1].is_type(STATE_TYPE_ROAD)
                        or self._board[row-1][col].is_type(STATE_TYPE_ROAD))
            return (self._board[row][col - 1].is_type(STATE_TYPE_ROAD)
                    or self._board[row][col + 1].is_type(STATE_TYPE_ROAD)
                    or self._board[row - 1][col].is_type(STATE_TYPE_ROAD))

        return (self._board[row][col-1].is_type(STATE_TYPE_ROAD)
                or self._board[row][col+1].is_type(STATE_TYPE_ROAD)
                or self._board[row-1][col].is_type(STATE_TYPE_ROAD)
                or self._board[row+1][col].is_type(STATE_TYPE_ROAD))

    def to_state(self, state: str, x: int, y: int):
        self._board[x][y].transition_to(False, state)

    def advance_time(self):
        for row in self._board:
            for col in row:
                col.advance_time(1)




