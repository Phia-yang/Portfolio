from turtle import *

room_position_for_rectangle = {'Kitchen':(-200, 190), 'Bathroom': (-20, 160), 'Dining Room': (180, 160), 'Master Room': (220, 190), 
                 'Library': (400, 160), 'Recreaction Room': (600, 160)}
room_position_for_text = {'Kitchen':(-195, 190), 'Bathroom': (-195, 50), 'Dining Room': (5, 50), 'Master Room': (225, 190), 
                 'Library': (225, 50), 'Recreaction Room': (425, 50)}

# ask the user what to do next
def prompt_question(title, question):
    ans = textinput(title, question)
    return ans

# print out the setting of this story
def print_setting(setting): 
    penup()
    goto(-660, -160)
    write(setting, font=("Arial", 12 , "normal"))

# print out the floor plan
def print_floorplan(): 
    penup()
    goto(-200, 360)
    # Courtyard
    print_rectangle('Courtyard', 'white', 380, 30) 
    goto(-200, 300)
    # 1st floor
    print_rectangle('1st floor', 'white', 380, 250)    
    forward(420)
    # 2nd floor
    print_rectangle('2nd floor', 'white', 380, 250)
    backward(180)
    # print 1st stairs
    print_rectangle('(stairs)', 'black', 90, 100)
    # print 2nd stairs
    forward(420)
    print_rectangle('(stairs)', 'black', 90, 100)
    print_room('Kitchen', 90, 110, 180, 20)
    print_room('Bathroom', 270, 110, 180, 20)
    print_room('Dining Room', 270, 110, 180, 20)
    print_room('Master Room', 90, 110, 180, 20)
    print_room('Library', 270, 110, 180, 20)
    print_room('Recreaction Room', 270, 110, 180, 20)
    for k in room_position_for_text.keys():
        print_room_text(k)

# remove the text as the user plays
def clean_text():
    penup()
    goto(-700, 400)
    color('white')
    print_rectangle('', 'white', 480, 1000)
    pendown()
    color('black')

# print out rectangles for floors and stairs
def print_rectangle(name, color, length, width):
    write(name, font=("Arial", 10 , "normal"))
    pendown()
    setheading(0)
    fillcolor(color) 
    begin_fill()
    for i in range(2):
        forward(length)
        right(90)
        forward(width)
        right(90)
    end_fill()
    penup()

# print out the room
def print_room(room, direction, length, width, door):
    penup()
    x, y = room_position_for_rectangle[room]
    goto(x, y)
    pendown()
    setheading(direction)
    forward(length)
    right(90)
    forward(width)
    right(90)
    forward(length)
    right(90)
    # draw the wall with a door
    forward((width-door)/2)
    penup()
    forward(door)
    pendown()
    forward((width-door)/2)

# print out the name of the room
def print_room_text(room): 
    penup()
    x, y = room_position_for_text[room]
    goto(x, y)
    pendown()
    write(room, font=("Arial", 10 , "normal"))

def print_conversation(title=None, content =None, options = None):
    clean_text()
    penup()
    #initial pos
    init_pos = (-660,300)
    goto(init_pos)
    title_pos = pos()
    x, y = title_pos
    
    # print the title
    if(title != None):
        pendown()
        write(title, move=True, align='left', font=('Arial', 18, 'normal')) 
    
    #print the content
    if(content != None):
        penup()
        content_y = y - 30
        
        goto(x, content_y) # init pos of content

        # print the content line by line
        x_right_boundry = -300
        first_line_pos = pos()
        line = 1
        content_list = content.split(" ")
        # print(content_list)
        for i in range(len(content_list)):
            curr_pos = pos()
            if("\n" in content_list[i]):
                temp_list = content_list[i].split("\n")
                new_word = temp_list[0] + " " + temp_list[1]
                content_list[i] = new_word
            if(xcor() >= x_right_boundry):
                next_line_y_axis = ycor() - 20
                setpos(first_line_pos[0], next_line_y_axis)
            write(content_list[i] + " ", move=True, align='left', font=('Arial', 14, 'normal')) 

    if(options != None):
        penup()
        curr_pos = pos()
        option_x_axis = init_pos[0]
        option_y_axis = ycor() - 40
        options_list = options.split("/")
        for i in range(len(options_list)):
            setpos(option_x_axis, option_y_axis)
            write(options_list[i], move=True, align='left', font=('Arial', 14, 'normal'))
            option_y_axis = option_y_axis - 20


def initialize():
    #print introduction
    # with open('introduction.txt', 'r',encoding='utf-8') as file:
    #     setting = file.read()
    #     print_setting(setting)
    speed(0)
    # # print setting
    # print_setting(setting)
    # print floor plan
    print_floorplan()

# # for testing
# ans = prompt_question('Test', 'What do you want?')
# print(ans)
# print_conversation("Servant", "The grand table makes its presence known in this room with its size. From one end to the other, this table is adorned with magnificently aged chairs. However, the table is half set up as if someone was interrupted in the middle of it. In this room, you can see: Family Insignia, Tableware, Windows",
#                    "1.dhuihds/2.dsfih/3.fdshic")
# print_conversation("Servant", "The grand table makes its presence known in this room with its size. From one end to the other, this table is adorned with magnificently aged chairs. However, the table is half set up as if someone was interrupted in the middle of it. In this room, you can see: Family Insignia, Tableware, Windows",
#                    "1.dhuihds/2.dsfih/3.fdshic")

