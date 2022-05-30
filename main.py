import curses
from curses import wrapper

class Menu:
    def __init__(self, stdscr, title, items):
        self.stdscr = stdscr
        self.title = title
        self.items = items

    def writeWord(self, y, x, word):
        self.stdscr.addstr(y, x, word[0], curses.A_UNDERLINE)
        self.stdscr.addstr(y, x+1, word[1:])

    def makeMenu(self):
        self.stdscr.clear()

        self.stdscr.addstr(3, 10, self.title)

        i = 5
        for item in self.items:
            self.writeWord(i, 10, item)
            i +=1

        self.stdscr.refresh()
        self.stdscr.getkey()

def main(stdscr):
    title = 'What do you want to do?'
    items = [ 'Pomodoro', 'Short Break', 'Long Break', 'Quit' ]
    mainMenu = Menu(stdscr, title, items)
    mainMenu.makeMenu()

wrapper(main)
