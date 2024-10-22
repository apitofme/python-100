"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Improved Quiz Game
"""


class QuizBrain:
    """Functionality to fetch questions and check answers"""

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
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

    def still_has_questions(self):
        """Returns Boolean for if there are questions remaining"""
        return self.question_number < len(self.question_list)

    def check_answer(self, player_answer, correct_answer):
        """Checks if the player's answer is correct, Returns Boolean"""
        if player_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's incorrect.")

        print(f"The correct answer is: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")
