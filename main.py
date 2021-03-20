import colorgram
import turtle
import random
from turtle import Turtle, Screen
manny = Turtle()
manny.speed(100)
manny.penup()
manny.hideturtle()

#######################################################################
#################use this to import colors from the file
# colors = colorgram.extract('damien-hirst-lactulose.jpg', 30)
# rgbcolors = []
# for color in colors:
#     #extract the individual colors
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgbcolors.append(new_color)
# print(rgbcolors)
turtle.colormode(255)
color_list = [(26, 109, 163), (193, 39, 81), (237, 161, 51), (234, 215, 86), (227, 237, 229), (222, 138, 176), (142, 109, 58), (102, 197, 218), (205, 165, 30), (21, 58, 132), (211, 74, 91), (237, 89, 52), (142, 208, 226), (119, 191, 140), (6, 158, 88), (5, 186, 179), (106, 108, 198), (137, 29, 72), (98, 51, 36), (25, 153, 211), (227, 169, 188), (151, 213, 195), (174, 186, 220), (234, 173, 162), (31, 90, 94), (84, 45, 34), (34, 45, 83)]
#########################################################################

manny.setheading(225)
manny.forward(300)
manny.setheading(0)
number_of_dots = 101


for num in range(1, number_of_dots):
    manny.dot(50, random.choice(color_list))
    manny.forward(70)
    if num % 10 == 0:
            manny.setheading(90)
            manny.forward(70)
            manny.setheading(180)
            manny.forward(700)
            manny.setheading(0)











































screen = Screen()
screen.exitonclick()