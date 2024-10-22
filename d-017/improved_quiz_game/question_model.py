"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-

Project: Improved Quiz Game

NOTE: Update this class to support the structure of the JSON data returned
via the Open Trivia Database API, e.g:

    {
        'type': 'boolean',
        'difficulty': 'medium',
        'category': 'General Knowledge',
        'question': 'Haggis is traditionally ate on Burns Night.',
        'correct_answer': 'True',
        'incorrect_answers': ['False']
    }
"""


class Question:
    """Provides the model for questions in the Quiz Game"""

    def __init__(self, question_dic):
        # Essentially we convert the incoming Dictionary in to an Object.
        # NOTE: This way is more flexible than using a DataClass!
        # ...However, given the modelling done in "data.py", this isn't really
        # necessary, since we only take the two data-components we need there.
        for k, v in question_dic.items():
            setattr(self, k, v)
