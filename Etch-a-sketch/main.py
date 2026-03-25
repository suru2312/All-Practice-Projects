from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_clockwise():
    tim.right(10)

def move_counter_clockwise():
    tim.left(10)

def clear_and_home():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_clockwise, "d")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(clear_and_home, "c")

screen.exitonclick()