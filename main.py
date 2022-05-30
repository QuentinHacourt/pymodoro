import curses
from curses import wrapper

def writeWord(y, x, word, stdscr):
    stdscr.addstr(y, x, word[0], curses.A_UNDERLINE)
    stdscr.addstr(y, x+1, word[1:])

def main(stdscr):
    stdscr.clear()
    begin_x = 20; begin_y = 7
    height = 5; width = 40
    win = curses.newwin(height, width, begin_y, begin_x)

    stdscr.addstr(3, 10, 'What do you want to do?')

    writeWord(5, 10, 'Pomodoro', stdscr)
    writeWord(6, 10, 'Short Break', stdscr)
    writeWord(7, 10, 'Long Break', stdscr)
    writeWord(8, 10, 'Quit', stdscr)

    stdscr.refresh()
    stdscr.getkey()

wrapper(main)
