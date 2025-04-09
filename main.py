from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Set up the screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)  # Turn off automatic screen updates

# Create paddles, ball, and scoreboard
left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
game_ball = Ball()
scoreboard = Scoreboard()

# Key bindings for paddle movement
screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

game_is_on = True

# Main game loop
while game_is_on:
    screen.update()
    game_ball.move()

    # Bounce the ball off top and bottom walls
    if game_ball.ycor() > 280 or game_ball.ycor() < -280:
        game_ball.bounce_y()

    # Detect collision with paddles
    if (game_ball.distance(right_paddle) < 50 and game_ball.xcor() > 320) or \
       (game_ball.distance(left_paddle) < 50 and game_ball.xcor() < -320):
        game_ball.bounce_x()

    # Right player misses
    if game_ball.xcor() > 380:
        game_ball.reset_position()
        scoreboard.left_point()

    # Left player misses
    elif game_ball.xcor() < -380:
        game_ball.reset_position()
        scoreboard.right_point()

screen.exitonclick()
