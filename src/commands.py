import curses
from src import windows, stats, util

class QUIT(Exception): pass

# Prompts user to enter command
def get_command(window):
    util.clearln(window, 1)
    window.addstr(0, 0, "                             ")
    window.addstr(0, 0, ">: ", curses.color_pair(windows.GREEN_PAIR))
    cmd = window.getstr(0, 3).decode('utf-8')
    util.clearln(window, 0)
    windows.draw_menu_window(window)
    do_command(cmd, window)
    return cmd

# Executes command given by get_command
def do_command(cmd, window):
    verb = ""
    noun = ""
    adjective = "1"
    if len(cmd.split()) == 3: verb, noun, adjective = cmd.split()
    elif len(cmd.split()) == 2: verb, noun = cmd.split()
    elif len(cmd.split()) == 1: verb = cmd.split()
    else: command_error(window)

    if cmd == "quit": quit_game(window); print("quiting...")
    elif verb == "buy":
        try:
            if noun == "miner": buy_worker(window, 'miner', int(adjective))
            elif noun == "farmer": buy_worker(window, 'farmer', int(adjective))
            elif noun == "woodcutter": buy_worker(window, 'woodcutter', int(adjective))
            else: command_error(window)
        except ValueError:
            value_error(window)
    elif cmd == "reset": reset(window)
    else: command_error(window)

def buy_worker(window, worker, amount = 1):
    costs = [
        stats.gold >= stats.worker_cost[worker]['gold'] * amount,
        stats.wheat >= stats.worker_cost[worker]['wheat'] * amount,
        stats.lumber >= stats.worker_cost[worker]['lumber'] * amount]

    if all(costs):
        stats.gold -= stats.worker_cost[worker]['gold'] * amount
        stats.wheat -= stats.worker_cost[worker]['wheat'] * amount
        stats.lumber -= stats.worker_cost[worker]['lumber'] * amount

        if worker == 'miner': stats.miners += amount
        elif worker == 'farmer': stats.farmers += amount
        elif worker == 'woodcutter': stats.woodcutters += amount

        util.clearln(window, 2)
    else: 
        util.clearln(window, 1)
        window.addstr(1, 0, "Not enough resources!", curses.color_pair(windows.ERROR_PAIR))

# Resets all stats to default
def reset(window):
    util.clearln(window, 0)
    window.addstr(0, 0, "Are you sure you want to reset?: ", curses.color_pair(windows.WARNING_PAIR))
    cmd = window.getstr(0, 33).decode('utf-8')
    util.clearln(window, 0)

    if cmd == "yes" or cmd == "y":
        stats.score = 0; stats.gold = 0; stats.wheat = 0; stats.lumber = 0
        stats.miners = 1
        stats.farmers = 0; stats.woodcutters = 0
        util.clearln(window, 2)
        util.clearln(window, 3)
        windows.draw_menu_window(window)
    elif cmd == "no": pass
    else: window.addstr(1, 0, "That is not a valid command!", curses.color_pair(windows.ERROR_PAIR))

def quit_game(window):
    window.addstr(1, 0, "Quiting...")
    raise QUIT

def command_error(window):
    window.addstr(1, 0, "That is not a valid command!", curses.color_pair(windows.ERROR_PAIR))

def value_error(window):
    window.addstr(1, 0, "Please enter an amount in numbers!", curses.color_pair(windows.ERROR_PAIR))