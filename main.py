import curses
from curses import wrapper
from time import sleep

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
        key = self.stdscr.getkey()
        self.handleChoice(key)

    def handleChoice(self, key):
        match key:
            case "p":
                timer = Timer(self.stdscr, "Pomodoro", 25, 0)
                timer.loop()
            case "q":
                quit()

        self.makeMenu()


class Timer:
    def __init__(self, stdscr, title, totalMinutes, totalSeconds):
        self.stdscr = stdscr
        self.title = title
        self.totalMinutes = totalMinutes
        self.totalSeconds = totalSeconds
        self.minutesLeft = totalMinutes
        self.secondsLeft = totalSeconds

    def loop(self):
        self.printTime()
        sleep(1)
        while(self.it()):
            self.printTime()
            sleep(1)

    def printTime(self):
        self.stdscr.clear()
        self.stdscr.addstr(3, 10, self.title)
        self.stdscr.addstr(5, 10, f'{self.formatTime(self.minutesLeft)}:{self.formatTime(self.secondsLeft)}')
        self.stdscr.refresh()

    def it(self):
        if self.secondsLeft == 0 and self.minutesLeft == 0:
            return False
        elif self.secondsLeft == 0:
            self.secondsLeft = 59
            self.minutesLeft -= 1
        else:
            self.secondsLeft -=1
        return True;

    def formatTime(self, time):
        if time >= 10:
            return str(time)

        return f"0{time}"


def main(stdscr):
    title = 'What do you want to do?'
    items = [ 'Pomodoro', 'Short Break', 'Long Break', 'Quit' ]
    mainMenu = Menu(stdscr, title, items)
    mainMenu.makeMenu()

wrapper(main)
