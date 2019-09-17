import curses
from src import windows, stats, commands
import shutil, time, threading

cols, rows = shutil.get_terminal_size(fallback=(80, 24))

def main():

    stdscr = curses.initscr()

    win = curses.newwin(rows -3, cols, 3, 0)
    statwin = curses.newwin(3, cols, 0, 0)

    windows.init_windows(win, statwin)

    win.refresh()
    statwin.refresh()
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

    curses.nocbreak()
    win.keypad(0)
    curses.echo()
    curses.endwin()  

def counter():
    try:
        while True:
            stats.gold += stats.workers
            time.sleep(1)
    except commands.QUIT: quit()

def run():
    main()

if __name__ == '__main__':
    curses.wrapper(main)