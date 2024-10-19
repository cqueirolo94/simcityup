import curses

GAME_NAME = 'SiMCiTY'

class GameRunner:
    def __init__(self):
        self.name = GAME_NAME

    def run(self):
        curses.wrapper(self.__run)

    def __run(self, stdscr):
        # Screen config.
        curses.curs_set(0)   # Hides the cursor.
        stdscr.nodelay(1)    # Doesn't wait for key press.
        stdscr.timeout(100)  # Refresh every 100ms.

        sh, sw = stdscr.getmaxyx()
        w = curses.newwin(sh, sw, 0, 0)
        w.keypad(True)

        # Player start position.
        player_pos = [sh // 2, sw // 2]

        key = curses.KEY_RIGHT
        while True:
            ####################################
            # Here goes the game state update. #
            ####################################
            next_key = w.getch()
            key = key if next_key == -1 else next_key

            # Moves player
            if key == curses.KEY_UP:
                player_pos[0] -= 1
            elif key == curses.KEY_DOWN:
                player_pos[0] += 1
            elif key == curses.KEY_LEFT:
                player_pos[1] -= 1
            elif key == curses.KEY_RIGHT:
                player_pos[1] += 1

            # Resets the screen.
            w.clear()
            w.addstr(player_pos[0], player_pos[1], 'O')
            w.refresh()

            # If 'q' is pressed it ends the game.
            if key == ord('q'):
                break
