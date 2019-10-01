import curses, locale
from src import stats, util

# Defines color and pair call numbers
DEFAULT_PAIR = 1
GREEN_PAIR = 2
WARNING_PAIR = 3
ERROR_PAIR = 4
GOLD_PAIR = 5
FARM_PAIR = 6
WOOD_PAIR = 7

COLOR_BLACK = 101
COLOR_WHITE = 102
COLOR_RED = 103
COLOR_GREEN = 104
COLOR_BLUE = 105
COLOR_YELLOW = 106
COLOR_ORANGE = 107

def draw_game_window(window):
    window.border()

def draw_menu_window(window):

    locale.setlocale(locale.LC_ALL, '') # Sets localization for number formating

    window.nodelay(1)

    window.addstr(0, 0, "Press TAB to enter a command.")

    window.addstr(2, 0, ("Gold: " + util.format_num(stats.gold)), curses.color_pair(GOLD_PAIR))
    window.addstr(2, 19, ("Wheat: " + util.format_num(stats.wheat)), curses.color_pair(FARM_PAIR))
    window.addstr(2, 39, ("Lumber: " + util.format_num(stats.lumber)), curses.color_pair(WOOD_PAIR))

    window.addstr(3, 0, ("Miners: " + util.format_num(stats.miners)), curses.color_pair(GOLD_PAIR))
    window.addstr(3, 19, ("Farmers: " + util.format_num(stats.farmers)), curses.color_pair(FARM_PAIR))
    window.addstr(3, 39, ("Woodcutters: " + util.format_num(stats.woodcutters)), curses.color_pair(WOOD_PAIR))

    window.addstr(0, 31, ("Score: " + util.format_num(stats.score)), curses.color_pair(DEFAULT_PAIR))

def init_windows(game_window, stat_window):

    curses.noecho()
    curses.cbreak()
    curses.curs_set(0)
    curses.start_color()

    init_colors()

    draw_game_window(game_window)
    draw_menu_window(stat_window)

    print("Windows initialized!")

def close_windows():

    curses.nocbreak()
    curses.echo()
    curses.endwin()

def init_colors(): # Defines colors and color pairs

    curses.init_color(COLOR_BLACK, 0, 0, 0)
    curses.init_color(COLOR_WHITE, 1000, 1000, 1000)
    curses.init_color(COLOR_RED, 1000, 0, 0)
    curses.init_color(COLOR_BLUE, 0, 0, 1000)
    curses.init_color(COLOR_GREEN, 0, 1000, 0)
    curses.init_color(COLOR_YELLOW, 1000, 1000, 0)
    curses.init_color(COLOR_ORANGE, 960, 740, 160)

    curses.init_pair(DEFAULT_PAIR, COLOR_WHITE, COLOR_BLACK)
    curses.init_pair(GREEN_PAIR, COLOR_GREEN, COLOR_BLACK)
    curses.init_pair(WARNING_PAIR, COLOR_YELLOW, COLOR_BLACK)
    curses.init_pair(ERROR_PAIR, COLOR_RED, COLOR_BLACK)
    curses.init_pair(GOLD_PAIR, COLOR_ORANGE, COLOR_BLACK)
    curses.init_pair(FARM_PAIR, COLOR_YELLOW, COLOR_BLACK)
    curses.init_pair(WOOD_PAIR, COLOR_GREEN, COLOR_BLACK)