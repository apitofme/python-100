"""
-=< 100 Days of Python >=-
-=[ Day 021 ]=-

Project: Build the 'Snake' Game
"""
from turtle import Screen
import time
from snake import Snake
from food import Food
"""
Snake Game - Part 2: Inheritance & List Slicing

Following from the previous day's lessons, we'll be continuing to add to our
Snake Game to build out the rest of the functionality, features and game logic.
NOTE: Finalising the migration to OOP, all classes are now separated out in to
their own module files!

> L.154 - Detect Collisions with Food
> L.155 - Create a Scoreboard and Keep Score
> L.156 - Detect Collisions with the Walls
> L.157 - Detect Collisions with the Sanke's Own Tail
"""

# Initialise and configure Screen object:
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Turtle: Snake Game")
# Turn animation off
window.tracer(0)
# NOTE: MUST manually call 'update()' to refresh the screen!

# Instantiate game objects:
snake = Snake()
food = Food()

window.update()

# Set up event listeners for key controls:
window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")
# window.onkey(snake.turn_left, "Left")
# window.onkey(snake.turn_right, "Right")

game_over = False
while not game_over:
    window.update()
    time.sleep(0.125)
    snake.move()
    # Detect collision with Food (Default: 15):
    if snake.head.distance(food) < 20:
        food.refresh()

window.exitonclick()
