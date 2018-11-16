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


#Function: food placement
def get_rand_food(sh,sw):
	food_x=random.randint(0,sw)
	food_y=random.randint(0,sh)
	scr.addstr(food_y,food_x,"$")
	scr.refresh()
	return food_y,food_x

def print_snake(snake):
	for var in snake:
		scr.addch(var[0],var[1],curses.ACS_CKBOARD)
	return


def check_food(snake,food_y,food_x,head):

	if head[0]==food_y and head[1]==food_x:
		food_y,food_x=get_rand_food(sh,sw)
	else:
		scr.addstr(snake[-1][0],snake[-1][1],' ')
		snake.pop()

	return food_y,food_x


food_x=0
food_y=0

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
food_y,food_x=get_rand_food(sh,sw)




#Infinite loop to control movement of the snake
while True:

	d=scr.getch()
	if d!=-1:
		var=d


	if var==curses.KEY_LEFT:
		head=[snake[0][0],snake[0][1]-1]

		food_y,food_x=check_food(snake,food_y,food_x,head)

		snake.insert(0,head)
		print_snake(snake)



	elif var==curses.KEY_RIGHT:
		head=[snake[0][0],snake[0][1]+1]

		food_y,food_x=check_food(snake,food_y,food_x,head)

		snake.insert(0,head)
		print_snake(snake)



	elif var==curses.KEY_UP:
		head=[snake[0][0]-1,snake[0][1]]

		food_y,food_x=check_food(snake,food_y,food_x,head)

		snake.insert(0,head)
		print_snake(snake)



	elif var==curses.KEY_DOWN:
		head=[snake[0][0]+1,snake[0][1]]

		food_y,food_x=check_food(snake,food_y,food_x,head)

		snake.insert(0,head)
		print_snake(snake)
