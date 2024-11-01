import curses
import random
import time
from curses import initscr, noecho, cbreak, start_color, echo, nocbreak, endwin
import datetime
import sys

from game.board import Board
from game.states.state import STATE_TYPE_HOUSE

GAME_NAME = 'SiMCiTY'
BOARD_ROWS = 10
BOARD_COLS = 10

class GameRunner:
    def __init__(self):
        self.name = GAME_NAME
        self.board = Board(BOARD_ROWS, BOARD_COLS)
        self.time = datetime.datetime.now()


    def run(self):
        while True:
            self.board.to_state(STATE_TYPE_HOUSE, random.randint(0,9),random.randint(0,9))
            sys.stdout.write("\r"+''.join(self.board.draw()))
            sys.stdout.flush()
            time.sleep(1)
