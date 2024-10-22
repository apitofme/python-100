"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Improved Quiz Game

L.125 - The Benefits of OOP: Using "Open Trivia DB" to Get New Questions

After completing the last lesson (L.124) our Quiz Game was fully playable,
using the pre-packaged set of questions, which were provided in the original
version of the "data.py" file. However, a quiz that always asks the player the
same questions is not a very good game. What would be better is if the game
asked a different, random set of questions each time it was played.

Thankfully there is a website called the "Open Trivia Database" that provides
an easy to use API (Application Programming Interface), allowing developers
access to a trivia database with over 4000 verified questions. We can access
this service via a URL and (best of all) it is completely FREE to use! [1]

The API provides several options that allow users to customise and filter the
selection of questions it will return, including choosing from a wide range of
categories, the relative difficulty level, and the format of the questions
(e.g. True/False). [2]

NOTE: The original challenge for this lesson was to use this API to grab a new
set of questions ONCE, copy and paste them below, then re-work the JSON data
in to a single Python dictionary, similar to that of the original questions.
Then re-work the game to use this new data-set instead.

However, I plan to implement the game such that everytime it is run it will
request a new set of questions from the API (if it is available), falling back
to the original set if not.

I may also add the ability for users to choose certain other options in order
to enhance the game, taking advantage of the options provided by the API,
e.g: the number of questions, rounds, the category, difficulty etc.

NOTE: Pythonistas would normally chooses to use the "request" library for this
task, and simply install it in their environment with `PIP`. However, since
the Python SDL does technically provide a library capable of performing URI
requests (in the form of `urllib.request`), I will implement it using this
instead. [3] & [4]

Refs:
[1] - https://opentdb.com
[2] - https://opentdb.com/api_config.php
[3] - https://docs.python.org/3.12/library/urllib.request.html#module-urllib.request
[4] - https://stackoverflow.com/a/77592494/632174
"""
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create list of Question objects from the question data
question_bank = []
for qd in question_data:
    question_bank.append(Question(qd))

# Create the QuizBrain object using the list created above
quiz = QuizBrain(question_bank)

# Loop game until there are no more questions
while quiz.still_has_questions():
    quiz.next_question()

# Show final score etc.
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")
