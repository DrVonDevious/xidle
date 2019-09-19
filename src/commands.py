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
    elif cmd == "buy miner": buy_miner(window)
    elif cmd == "buy farmer": buy_farmer(window)
    elif cmd == "buy woodcutter": buy_woodcutter(window)
    elif cmd == "reset": reset(window)
    else: command_error(window)

def buy_miner(window):
    if stats.gold >= 15:
        stats.gold -= 15
        stats.miners += 1
        util.clearln(window, 2)
    else: 
        util.clearln(window, 1)
        window.addstr(1, 0, "Not enough gold!")

def buy_farmer(window):
    if stats.gold >= 40:
        stats.gold -= 40
        stats.farmers += 1
        util.clearln(window, 2)
    else: 
        util.clearln(window, 1)
        window.addstr(1, 0, "Not enough gold!")

def buy_woodcutter(window):
    if stats.gold >= 100 & stats.wheat >= 20:
        stats.gold -= 100
        stats.wheat -= 20
        stats.woodcutters += 1
        util.clearln(window, 2)
    else: 
        util.clearln(window, 1)
        window.addstr(1, 0, "Not enough gold or lumber!")

def reset(window):
    util.clearln(window, 0)
    window.addstr(0, 0, "Are you sure you wish to reset?: ")
    cmd = window.getstr(0, 33).decode('utf-8')
    util.clearln(window, 0)

    if cmd == "yes":
        stats.score = 0
        stats.gold = 0
        stats.wheat = 0
        stats.lumber = 0
        stats.miners = 1
        stats.farmers = 0
        stats.woodcutters = 0
        util.clearln(window, 2)
        windows.draw_menu_window(window)
    elif cmd == "no": pass
    else: window.addstr(1, 0, "That is not a valid command!")

def quit_game(window):
    window.addstr(1, 0, "Quiting...")
    raise QUIT

def command_error(window):
    window.addstr(1, 0, "That is not a valid command!")