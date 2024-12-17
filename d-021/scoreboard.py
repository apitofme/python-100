"""
-=< 100 Days of Python >=-
-=[ Day 021 ]=-

Project: Build the 'Snake' Game
NOTE: For "Part 2" all OOP Classes are now in their own files!

>> L.155 - Create Scoreboard and Keep Score
"""
from turtle import Turtle


class Scoreboard(Turtle):
    """Class defining all attributes and methods relating to the Scoreboard
    object for the Snake Game"""

    ALIGNMENT = "center"
    FONT_FACE = "Terminal"
    FONT_SIZE = 14
    FONT_STYLE = "bold"

    def __init__(self):
        super().__init__()
        # Define Turtle properties for Scoreboard:
        self.hideturtle()
        self.color('white')
        self.penup()
        self.sety(280)
        # Setup game properties for Scoreboard:
        self.font = (self.FONT_FACE, self.FONT_SIZE, self.FONT_STYLE)
        self.score = 0
        # Display initial score:
        self.display()

    def increase(self, amount: int):
        """Increases the score by the given amount"""
        self.score += amount

    def display(self):
        """Displays the current score on the Screen"""
        # NOTE: First we must clear any previous score display!
        self.clear()
        self.write(
            f"SCORE: {self.score}",
            align=self.ALIGNMENT,
            font=self.font
        )

    def game_over(self):
        """Display the 'Game Over' message in the middle of the Screen"""
        self.sety(0)
        self.write(
            "GAME OVER",
            align=self.ALIGNMENT,
            font=self.font
        )

    def update(self, amount=1):
        """Increases the score and then displays it;
        -- Default increase amount = 1"""
        self.increase(amount)
        self.display()
