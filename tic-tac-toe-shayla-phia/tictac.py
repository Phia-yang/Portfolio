from turtle import *

fullboard = {
    '1': ['1', '2', '3'],
    '2': ['1', '2', '3'],
    '3': ['1', '2', '3']
}

keys_ = {
    '1': [],
    '2': [],
    '3': []
}



def board():
	speed(9)
	penup()
	forward(100)
	right(90)
	pensize(5)
	pendown()
	#first vertical line
	forward(300)
	penup()
	left(90)
	forward(100)
	left(90)
	pendown()
	#second vertical line
	forward(300)
	penup()
	right(90)
	forward(100)
	right(90)
	forward(100)
	right(90)
	#first horizontal line
	pendown()
	forward(300)	
	penup()
	left(90)
	forward(100)
	left(90)
	pendown()
	#second horizontal line
	forward(300)
	penup()
	goto(-300, 300)
	
def draw_x():
    penup()
    pencolor('cyan')
    right(45)
    forward(30)
    pendown()
    forward(80)
    penup()
    left((90+45))
    forward (56.569)
    left ((90+45))
    pendown()
    forward(80)
    penup()
    home()
    goto(-300,300)
  

def draw_o():
    penup()
    color('orange')
    forward(50)
    right(90)
    forward(10)
    pendown()
    right(90)
    circle(40)
    penup()
    home()
    goto(-300,300)
 


def goto_square(x, y):
	x = int(x)
	y = int(y)
	board_size = 300
	squares_across = 3
	
	board_x = -300 + (x-1) * (board_size / squares_across)
	board_y = 300 - (y-1) * (board_size / squares_across)
	penup()
	goto(board_x, board_y)
	pendown()
    
def user_input():
    color = "orange"
    while fullboard != keys_:
        x = textinput('column', "what column you would like to place your piece in?")
        y = textinput('row',  "what row  would you like to place your piece in?")
        goto_square(x,y)
        keys_[x].append(y)
        keys_[x].sort()
        color = next_color(color)
        


def next_color(current_color):
    if current_color == "cyan":
        draw_o()
        return "orange"
    if current_color == "orange":
        draw_x()  
        return "cyan" 
    pass



penup()
goto(-300, 300)
pendown()
board()
user_input()


done()