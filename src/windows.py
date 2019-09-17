import curses
from src import stats

def draw_game_window(window):
    window.border()

def draw_menu_window(window):
    window.nodelay(1)
    window.addstr(0, 0, "Press TAB to enter a command.")
    window.addstr(2, 0, ("Gold: " + str(stats.gold)))

def init_windows(game_window, stat_window):

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)

    draw_game_window(game_window)
    draw_menu_window(stat_window)

    print("Windows initialized!")