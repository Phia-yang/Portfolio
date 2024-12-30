from turtle import *
import sys
import string
import random

word_count = {}

def count_words(word_list):
    for word in word_list:
        word_count.setdefault(word, 0)
        word_count[word] += 1

input_filename = ""
if len(sys.argv) > 1:
	input_filename = sys.argv[1]
else:
	input_filename = "scaryscript.txt"

with open(input_filename, "r", encoding='utf-8') as f:
    line = f.read()
    while line != "":
        s = line.translate(str.maketrans('','',string.punctuation))
        word_list = s.lower().split()
        #print(word_list)  # Print to console
        line = f.read()
        count_words(word_list)

print (word_count)
i=0
p=0
screensize(400, 500)
cloud_type = textinput ("Word Cloud type", "I can generate a frequency (1), or an alphabetial word cloud (2). Select which word cloud with number 1 or 2")
if cloud_type == "1":
    sortedwordcount = sorted(word_count, key=word_count.get, reverse=True)
if cloud_type == "2":
    sortedwordcount = sorted(word_count)
penup()
goto(-300, 250)
for word in sortedwordcount:
    font_size = word_count[word]*2 + 8
    colors = ['midnight blue', 'medium blue', 'cornflower blue']
    if font_size >=24:
        color(colors[0])
        font_size = 26
    if font_size <24 and font_size >=14:
        color (colors[1])
    if font_size < 14:
        color (colors[2])
    homex = (xcor())
    homey = (ycor())
    write (word.lower(), move = True, font = ("Aloha", font_size, 'normal'))
    goto(homex, homey)
    right(90)
    forward(29)
    left (90)
    i += 1
    p += 1
    if i == 15:
        goto (-300+((p*6)), 250) #-250, -175, -100, -25
        i=0
    if p == 90:
        break
        
        
done()



