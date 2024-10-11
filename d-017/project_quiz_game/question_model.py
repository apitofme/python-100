"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Quiz Game
"""
"""
L.120 - Quiz Project Part 1: Creating the Question Class

Here we need to create a class to model the questions that we're going to use
in our Quiz Game. If we create a Question object, we can think about what kind
of attributes might it need to have?

There should perhaps be some kind of "text" attribute, to hold the text of the
question, and an "answer" attribute to hold the correct answer. Since we will
need to be able to display each question to the player, and then compare the
answer given with the known correct answer.

These attributes will need to be initialised with their values whenever a new
Question object is created from this class. For example, if a question was
"2 + 3 = 5", and we know the answer is "True", then the code might look like
the following: `new_q = Question("2 + 3 = 5", "True")`

So, the constructor for the 'Question' class should take values for both of
these attributes as arguments and store the given values on them. We are then
able to reference those values on the Object later, e.g. with `new_q.text`
"""


class Question:
    """Provides the model for questions in the Quiz Game"""

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
