"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Quiz Game
"""
"""
L.121 - Quiz Project Part 2: Creating a List of Question Objects from the Data

This file provides a set of questions we can use in our quiz game, complete
with their answers. These are presented in the form of a List of Dictionaries,
where each dictionary contains two entries with the keys "text" and "answer"
respectively.

The first thing we need to do is format the list correctly, by indenting each
entry inside the list's square brackets. We will also need to deal with lines
that are too long (see note below), which we can do by simply breaking the
line up so that it is split across two seaparate lines. These must maintain
the correct indentation, and both parts must be wrapped in their own set of
quotation marks (i.e. you cannot have opening and closing quotation marks on
separate lines). - This works because in Python adjacent string literals are
automatically joint together by the interpreter into a single string.

NOTE: The Style Guide for Python Code [PEP8] 'prefers' lines which are less
than 80 characters long! (i.e. a maximum of 79 characters)
Ref: https://peps.python.org/pep-0008/#maximum-line-length

The next part of this challenge will be to turn this list of questions in to
a list of Question objects to create a 'question bank' for the game's code to
use -- This will need to implemented in the "man.py" file!
"""
question_data = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.",
     "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.",
     "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a "
     "football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with "
     "your car, you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of "
     "Parliament, you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.",
     "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.",
     "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.",
     "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than "
     "7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.",
     "answer": "True"}
]
