"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Quiz Game
"""
"""
L.122 - Quiz Project Part 3: The QuizBrain Class and next_question() Method

In "Part 1" of today's lessons we created the Question class definition inside
the "question_model.py" file. Then in "Part 2" we tidied up the game data, a
pre-compiled list of questions with their correct answers, and converted the
raw data in to a series of Question objects which we stored in a variable
called "question_bank". Now that we have both of these tasks complete we're
ready to figure out how were going to actually display one of these Questions
to the user and ask them to answer it. To do this were going to start to build
the "QuizBrain" class here.

This "QuizBrain" class will handle all of game functionality and logic needed
in order to present the game to the player. To do this it will need to be able
to perform the following tasks:

    1. Ask the questions to the player
    2. Check if the answer given by the player was correct
    3. Check if we've reached the end of the quiz

So it will probably need a couple of attributes, one to track which question
we're currently on and another to hold the actual list of questions. It will
also need a method which should enable us to get the next question from the
list, based on the current question number we're on.
"""


class QuizBrain:
    """Functionality to fetch questions and check answers"""

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        """Asks the next Question object from the question list;
        Checks the given answer using the `check_answer()` method;
        Keeps track of the score by updating `self.score`"""
        # get the Question object for the current question number
        question = self.question_list[self.question_number]

        # update the question number ready for the next question
        self.question_number += 1

        # display the question (should be in "main.py" IMO)
        answer = input(
            f"Q.{self.question_number}: {question.text} True/False? "
        ).lower()

        # check if the given answer was correct
        self.check_answer(answer, question.answer)
        # return question
        # return answer

    """
    L.123 - Quiz Project Part 4: How to keep showing new Questions
        
        1. Add a method "still_has_questions()" to the QuizBrain class
        2. (see "main.py")
    """

    def still_has_questions(self):
        """Returns Boolean for if there are questions remaining"""
        return self.question_number < len(self.question_list)

    """
    L.124 - Quiz Project Part 5: Checking Answers and Keeping Score

        1. Add a new method to check if the player's answer is correct
        2. Add a new attribute to keep track of the player's score
        3. Make sure the score is updated every time the player is correct
        4. Show the player their result, the correct answer and their score
        5. (see "main.py")
    """

    def check_answer(self, player_answer, correct_answer):
        """Checks if the player's answer is correct, Returns Boolean"""
        if player_answer.lower() == correct_answer.lower():
            print("You got it right!")
            # update the score
            self.score += 1
        else:
            print("That's incorrect.")
        # show the correct answer
        print(f"The correct answer is: {correct_answer}")
        # show the player's current score (out of # of Q's asked)
        print(f"Your current score is: {self.score}/{self.question_number}\n")
