# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_color)


import turtle as Turtle_module
from turtle import Screen
import random

Turtle_module.colormode(255)
tim = Turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(195, 165, 122), (139, 83, 62), (220, 201, 141), (64, 94, 117), (141, 163, 178), (163, 151, 57), (125, 36, 27), (69, 36, 31), (54, 116, 89), (148, 178, 155), (182, 102, 90), (34, 58, 72), (164, 147, 157), (225, 177, 168), (22, 89, 69), (110, 75, 77), (142, 21, 25), (16, 68, 57), (89, 146, 125), (184, 92, 96), (179, 202, 183), (24, 83, 86), (84, 30, 32), (110, 127, 150), (36, 65, 100), (183, 190, 205)]
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()
