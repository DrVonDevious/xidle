import curses
from src import windows, stats, util

class QUIT(Exception): pass

def get_command(window):

    util.clearln(window, 0)
    util.clearln(window, 1)
    window.addstr(0, 0, ">: ")
    cmd = window.getstr(0, 3).decode('utf-8')
    util.clearln(window, 0)
    windows.draw_menu_window(window)
    do_command(cmd, window)
    return cmd

def do_command(cmd, window):

    if cmd == "quit": quit_game(window); print("quiting...")
    elif cmd == "buy": buy(window)
    else: command_error(window)

def buy(window):
    stats.gold -= 15
    stats.workers += 1
    util.clearln(window, 2)

def sell(n):
    pass

def say(window, msg):
    window.addstr(msg)

def quit_game(window):
    window.addstr(1, 0, "Quiting...")
    raise QUIT

def command_error(window):
    window.addstr(1, 0, "That is not a valid command!")