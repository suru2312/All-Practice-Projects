from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title = "Make the bet", prompt = "Which turtle will win the race? Choose your color : ").lower().strip()
colors = ["red", "green", "blue", "cyan", "yellow", "purple"]

y_positions = [20, 60, 100, -20, -60, -100]
turtles = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=y_positions[i])
    turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for t in turtles:
        if t.xcor() >= 210:
            is_race_on = False
            winning_color = t.pencolor()
            if winning_color == user_bet:
                print(f"You've Won! The {winning_color} turtle won the race.")
            else:
                print(f"You've Lost! The {winning_color} turtle won the race.")
            break
        
        random_distance = random.randint(0,10)
        t.forward(random_distance)

screen.exitonclick()