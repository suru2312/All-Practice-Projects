from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
SCREEN_SIZE = 600
MOVE_DELAY = 0.1
WALL_LIMIT = 290

def setup_screen():
    screen = Screen()
    screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.tracer(0)
    return screen

def setup_controls(screen, snake):
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

def check_food_collision(snake, food, scoreboard):
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

def check_wall_collision(snake):
    if snake.head.xcor() > WALL_LIMIT or snake.head.xcor() < -WALL_LIMIT:
        return True
    if snake.head.ycor() > WALL_LIMIT or snake.head.ycor() < -WALL_LIMIT:
        return True
    return False

def check_tail_collision(snake):
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            return True
    return False

def main():
    screen = setup_screen()
    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()
    setup_controls(screen, snake)
    
    game_is_on = True

    while game_is_on:
        screen.update()
        time.sleep(MOVE_DELAY)
        snake.move()

        # Collisions
        check_food_collision(snake, food, scoreboard)

        if check_wall_collision(snake) or check_tail_collision(snake):
            scoreboard.reset()
            snake.reset()

    screen.exitonclick()

if __name__ == "__main__":
    main()