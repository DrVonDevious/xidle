import curses
from src import stats

def draw_game_window(window):
    window.border()

def draw_menu_window(window):

    window.nodelay(1)

    window.addstr(0, 0, "Press TAB to enter a command.")

    window.addstr(2, 0, ("Gold: " + str(stats.gold)))
    window.addstr(2, 15, ("Wheat: " + str(stats.wheat)))
    window.addstr(2, 31, ("Lumber: " + str(stats.lumber)))

    window.addstr(2, 48, ("Miners: " + str(stats.miners)))
    window.addstr(2, 65, ("Farmers: " + str(stats.farmers)))
    window.addstr(2, 83, ("Woodcutters: " + str(stats.woodcutters)))

    window.addstr(2, 105, ("Score: " + str(stats.score)))

def init_windows(game_window, stat_window):

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()

    draw_game_window(game_window)
    draw_menu_window(stat_window)

    print("Windows initialized!")

def close_windows():

    curses.nocbreak()
    curses.echo()
    curses.endwin()