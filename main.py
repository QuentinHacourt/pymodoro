import curses
from curses import wrapper

def writeWord(y, x, word, stdscr):
    stdscr.addstr(y, x, word[0], curses.A_UNDERLINE)
    stdscr.addstr(y, x+1, word[1:])

def main(stdscr):
    stdscr.clear()

    stdscr.addstr(3, 10, mainMenuTitle)

    i = 5
    for menuItem in mainMenuItems:
        writeWord(i, 10, menuItem, stdscr)
        i +=1

    stdscr.refresh()
    stdscr.getkey()


mainMenuTitle = 'What do you want to do?'
mainMenuItems = [ 'Pomodoro', 'Short Break', 'Long Break', 'Quit' ]
wrapper(main)
