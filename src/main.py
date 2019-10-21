import curses
from src import windows, stats, commands, util
import shutil, time, threading, sys
from src.data import data_handling

cols, rows = shutil.get_terminal_size(fallback=(80, 24))
running = False

def main():

    data_handling.login()

    global running

    stdscr = curses.initscr()

    try: # Initial load
        data_handling.load()
    except:
        data_handling.save()
        data_handling.load()

    # Sets sub-window sizes
    statwin = curses.newwin(4, cols, 0, 0)

    windows.init_windows(statwin)

    statwin.refresh()
    running = True

    # Starts a seperate thread for the counter
    counter_thread = threading.Thread(target = counter)
    counter_thread.start()

    # Main loop
    try:
        while True:

            windows.draw_menu_window(statwin)
            if statwin.getch() == 9: curses.echo(); curses.curs_set(1); commands.get_command(statwin)
            curses.noecho(); curses.curs_set(0)

            statwin.refresh()

    except commands.QUIT: print("Quiting...")

    running = False
    data_handling.save()

    windows.close_windows()
    sys.exit()

# Counter updates every 1/100th of a second
def counter():
    try:
        while running == True:

            stats.score += (stats.miners + stats.farmers + stats.woodcutters) / 100

            stats.gold += stats.miners / 100
            stats.wheat += stats.farmers / 100
            stats.lumber += stats.woodcutters / 100

            time.sleep(0.01)

    except commands.QUIT: print("Closed counter!")

def run():
    main()