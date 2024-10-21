"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Quiz Game

Using everything we've learnt so far about OOP, creating Classes and adding
Attributes and Methods, we're going to build a simple quiz game where players
are asked a series of True/False questions.

The program will need to display a question and prompt the user for their
answer, check their answer and update the score accordingly. Repeating the
process to ask more questions, whilst keeping track of the overall score.

NOTE: This project is completed over the course of several lessons, each
tackling a different part of the problem. These may focus on a single specific
file, or spread tasks across multiple files. I will do my best to keep notes
appropriately.
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create the bank of questions for the quiz game [L.121]
question_bank = []
for qd in question_data:
    question_bank.append(Question(qd['text'], qd['answer']))

# print(question_bank[0].text)
# print(question_bank[0].answer)

"""
L.123 - Quiz Project Part 4: How to keep showing new Questions

    1. (see "quiz_brain.py")
    2. Create loop to keep calling the "next_question()" method until there
       are no questions left in the 'question_list'.
"""
quiz = QuizBrain(question_bank)
# print(f"Total # Qs: {len(quiz.question_list)}")
# print(f"Q#: {quiz.question_number}")
while quiz.still_has_questions():
    quiz.next_question()

"""
L.124 - Quiz Project Part 5: Checking Answers and Keeping Score
    
    1-4. (see "quiz_brain.py")
    5. Show the total score at the end of the quiz (out of total Q's)
"""
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
