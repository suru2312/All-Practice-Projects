from turtle import Turtle, Screen
import pandas as pd

screen = Screen()
screen.title("U.S. States Game")

image = r"D:\Python Bootcamp\Day25\US States Game\blank_states_img.gif"
screen.addshape(image)

map_turtle = Turtle()
map_turtle.shape(image)

dataset = pd.read_csv(r"D:\Python Bootcamp\Day25\US States Game\50_states.csv")
all_states = dataset["state"].to_list()

guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 Correct",
        prompt="Name the State"
    )

    if answer_state is None or answer_state.title() == "Exit":
        break

    answer_state = answer_state.title()

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        t = Turtle()
        t.hideturtle()
        t.penup()

        state_data = dataset[dataset["state"] == answer_state]
        t.goto(state_data["x"].item(), state_data["y"].item())
        t.write(answer_state)

# ✅ Game Over Screen
game_over = Turtle()
game_over.hideturtle()
game_over.penup()
game_over.goto(0, 0)

game_over.write(
    f"Game Over\nScore: {len(guessed_states)}/50",
    align="center",
    font=("Courier", 20, "normal")
)

screen.exitonclick()