import turtle as turtle_module
import random

turtle_module.colormode(255)

t = turtle_module.Turtle()
t.speed(0)
t.hideturtle()

color_list = [(198, 173, 119), (214, 225, 218), (162, 100, 54), (126, 35, 23),
            (185, 158, 50), (5, 55, 83), (51, 32, 28), (110, 68, 86),
            (116, 162, 176), (22, 120, 171), (76, 34, 43), (66, 154, 132),
            (83, 140, 64), (7, 65, 44), (184, 97, 79), (128, 37, 41),
            (204, 201, 147), (145, 178, 162), (174, 152, 157),
            (177, 201, 185), (219, 182, 168), (25, 80, 60)]

t.penup()
t.setheading(225)
t.forward(300)
t.setheading(0)

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(40)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(40)
        t.setheading(180)
        t.forward(400)
        t.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()