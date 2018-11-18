import curses
import random



def get_rand_food(sh,sw,snake):
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
		food_y,food_x=get_rand_food(sh,sw,snake)
	else:
		scr.addstr(snake[-1][0],snake[-1][1],' ')
		snake.pop()

	return food_y,food_x

def check_lost(snake,head):
	for var in snake:
		if head[0]==var[0] and head[1]==var[1]:
			curses.endwin()
			quit()
	return


#Screen Initialization
win=curses.initscr()
curses.curs_set(0)
curses.noecho()
sh,sw=win.getmaxyx()
scr=curses.newwin(sh,sw,0,0)
scr.keypad(True)
scr.timeout(60) 

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
food_y,food_x=get_rand_food(sh,sw,snake)
var=curses.KEY_RIGHT
#Infinite loop to control movement of the snake
while True:
	d=scr.getch()
	if d!=-1:
		if var==curses.KEY_LEFT and d!=curses.KEY_RIGHT:
			var=d
		elif var==curses.KEY_RIGHT and d!=curses.KEY_LEFT:
			var=d
		elif var==curses.KEY_UP and d!=curses.KEY_DOWN:
			var=d
		elif var==curses.KEY_DOWN and d!=curses.KEY_UP:
			var=d

	if var==curses.KEY_LEFT:
		head=[snake[0][0],snake[0][1]-1]
		check_lost(snake,head)
		food_y,food_x=check_food(snake,food_y,food_x,head)
		snake.insert(0,head)
		print_snake(snake)

	elif var==curses.KEY_RIGHT:
		head=[snake[0][0],snake[0][1]+1]
		check_lost(snake,head)
		food_y,food_x=check_food(snake,food_y,food_x,head)
		snake.insert(0,head)
		print_snake(snake)

	elif var==curses.KEY_UP:
		head=[snake[0][0]-1,snake[0][1]]
		check_lost(snake,head)
		food_y,food_x=check_food(snake,food_y,food_x,head)
		snake.insert(0,head)
		print_snake(snake)

	elif var==curses.KEY_DOWN:
		head=[snake[0][0]+1,snake[0][1]]
		check_lost(snake,head)
		food_y,food_x=check_food(snake,food_y,food_x,head)
		snake.insert(0,head)
		print_snake(snake)
