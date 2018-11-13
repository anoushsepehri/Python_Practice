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
	food_x=random.randint(0,sw)
	food_y=random.randint(0,sh)
	scr.addstr(food_y,food_x,"$")
	scr.refresh()
	return

def print_snake(snake):
	#scr.clear()
	i=0
	while i<4:
		scr.addch(snake[i][0],snake[i][1],curses.ACS_CKBOARD)
		i+=1
	return

def move_snake(var):
	if var==curses.KEY_LEFT:
		head=[snake[0][0],snake[0][1]-1]
		scr.addstr(snake[3][0],snake[3][1]," ")
		snake.insert(0,head)
		print_snake(snake)

	elif var==curses.KEY_RIGHT:
		head=[snake[0][0],snake[0][1]+1]
		scr.addstr(snake[3][0],snake[3][1]," ")
		snake.insert(0,head)
		print_snake(snake)

	elif var==curses.KEY_UP:
		head=[snake[0][0]-1,snake[0][1]]
		scr.addstr(snake[3][0],snake[3][1]," ")
		snake.insert(0,head)
		print_snake(snake)

	elif var==curses.KEY_DOWN:
		head=[snake[0][0]+1,snake[0][1]]
		scr.addstr(snake[3][0],snake[3][1]," ")
		snake.insert(0,head)
		print_snake(snake)
	return


#SNAKE INITIALIZATION
snk_y=10
snk_x=30
snake=[
[snk_y,snk_x],
[snk_y,snk_x-1],
[snk_y,snk_x-2],
[snk_y,snk_x-3]
]

#SETUP STARTING SCENE
print_snake(snake)
var=scr.getch()
get_rand_food(sh,sw)



#Infinite loop to dcontrol movement of the snake
while True:

	d=scr.getch()
	if d!=-1:
		var=d

	move_snake(var)



