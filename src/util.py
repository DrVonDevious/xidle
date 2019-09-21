import curses

def clearln(window, row): # Clears a single line

    x, y = window.getyx()
    window.move(row, 0)
    window.clrtoeol()
    window.move(x, y)