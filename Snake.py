import curses
import time
import random

win=curses.initscr()
curses.curs_set(0)
win.keypad(1)

sh,sw=win.getmaxyx()
scr=curses.newwin(sh,sw,0,0)
#scr.timeout(100) 



def get_rand_food(sh,sw):
	scr.clear()

	food_x=random.randint(0,sw)
	food_y=random.randint(0,sh)
	scr.addstr(food_y,food_x,"$")
	scr.refresh()
	return



while (1):
	get_rand_food(sh,sw)
	time.sleep(2)
