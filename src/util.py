import curses

def clearln(window, row): # Clears a single line

    x, y = window.getyx()
    window.move(row, 0)
    window.clrtoeol()
    window.move(x, y)
    
def addclstr(window, row, col, str, fcolor, bcolor):
    #win = curses.getwin()
    curses.init_pair(1, fcolor, bcolor)
    window.addstr(row, col, str, curses.color_pair(1))
    #curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)