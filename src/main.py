import curses
from src import windows, stats, commands, util
import shutil, time, threading, sys
from src.data import data_handling

cols, rows = shutil.get_terminal_size(fallback=(80, 24))
running = False

def main():

    global running

    stdscr = curses.initscr()

    try:
        data_handling.load()
    except:
        data_handling.save()
        data_handling.load()

    win = curses.newwin(rows -3, cols, 3, 0)
    statwin = curses.newwin(3, cols, 0, 0)

    windows.init_windows(win, statwin)

    win.refresh()
    statwin.refresh()
    running = True
    counter_thread = threading.Thread(target = counter)
    counter_thread.start()

    try:
        while True:

            windows.draw_menu_window(statwin)
            if statwin.getch() == 9: curses.echo(); curses.curs_set(1); commands.get_command(statwin)
            curses.noecho(); curses.curs_set(0)

            win.refresh()
            statwin.refresh()

    except commands.QUIT: print("Quiting...")

    running = False
    data_handling.save()

    windows.close_windows()
    sys.exit()

def counter():
    try:
        while running == True:

            stats.score += stats.miners + stats.farmers + stats.woodcutters

            stats.gold += stats.miners
            stats.wheat += stats.farmers
            stats.lumber += stats.woodcutters

            time.sleep(1)

    except commands.QUIT: print("Closed counter!")

def run():
    main()