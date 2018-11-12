import curses
import time
import random
import math

win=curses.initscr()
curses.curs_set(0)
curses.noecho()

sh,sw=win.getmaxyx()
scr=curses.newwin(sh,sw,0,0)
scr.keypad(True)
scr.timeout(100) 



def get_rand_food(sh,sw):
	scr.clear()

	food_x=random.randint(0,sw)
	food_y=random.randint(0,sh)
	scr.addstr(food_y,food_x,"$")
	scr.refresh()
	return

#getch testings implement later
while True:
	var=scr.getch()
	if var==curses.KEY_LEFT:
		scr.clear()
		scr.addstr(20,20,"left key")

	elif var==curses.KEY_RIGHT:
		scr.clear()
		scr.addstr(20,20,"right key")


