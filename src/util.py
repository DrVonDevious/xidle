import curses

def clearln(window, row): # Clears a single line

    x, y = window.getyx()
    window.move(row, 0)
    window.clrtoeol()
    window.move(x, y)

def format_num(num):

    num_digits = len(str(int(num)))
    text = str("{:n}".format(int(num)))
    
    #TODO: Simplify this block of code. Can be done by plugging in num_digits and the divisor and returing the abbreviation.
    if num_digits >= 7 and num_digits < 10: text = str("{:n}".format(float(num / 10**6)) + "M")
    elif num_digits >= 10 and num_digits < 13: text = str("{:n}".format(float(num / 10**9)) + "B")
    elif num_digits >= 13 and num_digits < 16: text = str("{:n}".format(float(num / 10**12)) + "T")
    elif num_digits >= 16 and num_digits < 19: text = str("{:n}".format(float(num / 10**15)) + "Qa")
    elif num_digits >= 19 and num_digits < 22: text = str("{:n}".format(float(num / 10**18)) + "Qi")
    elif num_digits >= 22 and num_digits < 25: text = str("{:n}".format(float(num / 10**21)) + "Sx")
    elif num_digits >= 25 and num_digits < 28: text = str("{:n}".format(float(num / 10**24)) + "Sp")
    elif num_digits >= 28 and num_digits < 31: text = str("{:n}".format(float(num / 10**27)) + "Oc")
    elif num_digits >= 31 and num_digits < 34: text = str("{:n}".format(float(num / 10**30)) + "No")
    elif num_digits >= 34 and num_digits < 37: text = str("{:n}".format(float(num / 10**33)) + "Dc")
    elif num_digits >= 37 and num_digits < 40: text = str("{:n}".format(float(num / 10**36)) + "Ud")
    elif num_digits >= 40 and num_digits < 43: text = str("{:n}".format(float(num / 10**39)) + "Dd")
    elif num_digits >= 43 and num_digits < 46: text = str("{:n}".format(float(num / 10**42)) + "Td")
    elif num_digits >= 46 and num_digits < 49: text = str("{:n}".format(float(num / 10**45)) + "Qad")
    elif num_digits >= 49 and num_digits < 52: text = str("{:n}".format(float(num / 10**48)) + "Qid")
    return text