from turtle import Screen
from paddle import Paddle
import time
from ball import Ball
from scoreboard import Scoreboard

# CONSTANTS
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
P1_STARTING_POS = (-400, 0)
P2_STARTING_POS = (400, 0)
BALL_START_POSITION = (0,0)


def screen_setup():
    screen = Screen()
    screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)
    return screen

def main():
    screen = screen_setup()
    l_paddle = Paddle(P1_STARTING_POS)
    r_paddle = Paddle(P2_STARTING_POS)
    scoreboard = Scoreboard()
    
    screen.listen()
    # Player 1 movement
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")
    # Player 2 movement
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    
    ball = Ball(BALL_START_POSITION)
    
    game_is_on = True
    
    while game_is_on:
        screen.update()
        time.sleep(ball.move_speed)
        ball.move()
        
        # Detect collision with the ball
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        
        # Detect collision with Paddle
        if (ball.distance(r_paddle) < 50 and ball.xcor() > 370) or (ball.distance(l_paddle) < 50 and ball.xcor() > -390):
            ball.bounce_x()
        
        # Detect R Paddle misses
        if ball.xcor() > 400:
            ball.reset_ball_position()
            scoreboard.l_point()
        
        # Detect L Paddle misses
        if ball.xcor() < -400:
            ball.reset_ball_position()
            scoreboard.r_point()
    
    screen.exitonclick()

if __name__ == "__main__":
    main()