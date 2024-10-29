"""
-=< 100 Days of Python >=-
-=[ Day 018 ]=-
"""
import random
from turtle import Turtle, Screen
"""
L.133 - Turtle Challenge 4: Generate a Random Walk
"""
pen = Turtle()
window = Screen()

# Pre drawing set up
window.colormode(255)
pen.down()
pen.speed(8)
pen.width(5)
directions = [
    (0, 'East'),
    (90, 'North'),
    (180, 'West'),
    (270, 'South')
]

# basic concept for random walk, before watching video intro
for _ in range(100):
    distance = random.randint(10, 50)
    # direction = random.randint(0, 365)
    bearing, direction = random.choice(directions)
    colour = (r, g, b) = random.sample(range(0, 255), 3)
    pen.color(colour)
    pen.forward(distance)
    pen.left(bearing)
    # Document the walk to allow recreating it:
    print(f"Turtle walked {distance} paces, heading {direction}")

# Keep the display window open until we click on it
window.exitonclick()
