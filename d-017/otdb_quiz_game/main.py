"""
Open Trivia DB Quiz Game

This implementation of the Quiz Game project utilises a package called
"opentriviadb", which handles all of the interactions with the OpenTriviaDB
API (including session tokens and caching!). You can install this package
from PyPI using `pip` (reference link below).

With the package installed, all that's left to do is implement the game logic,
output and flow (fingers crossed).

Ref: https://pypi.org/project/opentriviadb/
"""
import asyncio
from dataclasses import dataclass
import requests
from opentriviadb import Client, Category
from opentriviadb.errors import NoResults, TokenEmpty, TokenNotFound

MAX_ROUNDS = 5
MAX_QUESTIONS = 20
E_PROMPT = "Invalid response!"


@dataclass
class TriviaCategory:
    """Model for individual Categories provided by OpenTriviaDB"""
    id: int
    name: str


class Validate:
    """Container for various validation functions to sanitise user input"""

    BOOL_TRUE = ['true', 't', 'yes', 'y', '1']
    BOOL_FALSE = ['false', 'f', 'no', 'n', '0']

    @staticmethod
    def eval_boolean(value):
        """Evaluates the given value as a Boolean and returns it
        (i.e. Returns the explicit Boolean interpretation of 'value')
        """
        if value in Validate.BOOL_TRUE:
            return True
        if value in Validate.BOOL_FALSE:
            return False
        raise ValueError(f'Unable to evaluate value "{value}" as Boolean')

    @staticmethod
    def as_boolean(value):
        """Validates the given value as any acceptable Boolean value,
        Does NOT evaluate the actual Boolean value!
        (i.e. can 'value' be interpreted as a Boolean, even if it's "False")
        Returns Boolean"""
        if value in Validate.BOOL_TRUE or value in Validate.BOOL_FALSE:
            return True
        return False

    @staticmethod
    def as_integer(value):
        """Returns True if value is a whole number, False otherwise"""
        if isinstance(value, str):
            return value.isdigit()
        return isinstance(value, int)

    @staticmethod
    def is_less_than(value, test):
        """Compares 'value' with 'test', Returns Boolean"""
        return float(value) < float(test)

    @staticmethod
    def is_greater_than(value, test):
        """Compares 'value' with 'test', Returns Boolean"""
        return float(value) > float(test)

    @staticmethod
    def is_greater_than_zero(value):
        """Returns True if value is a number greater than zero,
        False otherwise"""
        return float(value) > 0

    @staticmethod
    def is_between(value, lower, upper):
        """Check if an integer number is between 'lower' and 'upper' values"""
        return float(lower) < float(value) < float(upper)


def is_valid(validation, value, *args, **kwargs):
    """
    Calls one or more validation functions with given argument parameters,
    Multiple validations call *this* function recursively, allowing a single
    return value (i.e. if any single validation fails, returns 'False')

    validation -> callable function to use for validation
    validation -> list of callable functions, for multiple validations
        Format: [
            simple_func,
            (func_with_args, [*args]),
            (func_with_kwargs, {**kwargs})
        ]
    value -> the value to validate (i.e. a String from user input)
    *args -> optional positional arguments to pass
    **kwargs -> optional keyword arguments to pass

    Returns Boolean
    """
    # If no function is given just confirm there is a "truthy" value
    if validation is None:
        if value:
            return True
        return False

    # NOTE: Prevent "PyLint: Too many return statements" by using a 'flag'
    valid = True

    # Single validation function:
    if callable(validation):
        valid = validation(value, *args, **kwargs)

    # Single function with one or more arguments
    elif isinstance(validation, tuple):
        v_func, v_args = validation
        # - Multiple positional arguments
        if isinstance(v_args, list):
            valid = is_valid(v_func, value, *v_args)
        # - Multiple keyword arguments
        elif isinstance(v_args, dict):
            valid = is_valid(v_func, value, **v_args)
        # - Single argument
        else:
            valid = is_valid(v_func, value, v_args)

    # Multiple validation functions to call:
    elif isinstance(validation, list):
        for item in validation:
            # Call *this* function recursively
            if not is_valid(item, value, *args, **kwargs):
                # Catch a failed validation and exit early!
                return False
        # If loop completes then all validations passed
        return True

    else:
        # ERROR: passed an invalid type
        raise TypeError(
            f'Function "Validation" does not accept "{type(validation)}" Type!'
            '-- Please read the function docstring.'
        )

    return valid


def ask(question, error_msg=E_PROMPT, validation=None, expects=str):
    """Asks the user the question, takes their input and passes it off for
    validation, Returns the expected format or a String"""
    valid = False
    while not valid:
        answer = input(question).lower()
        # print(f"Answer: {answer}")
        valid = is_valid(validation, answer)
        if not valid:
            print(error_msg)

    # Provide the required return type format...
    # Convert answer to a Boolean, i.e.
    # -- 'true' / 't' / 'yes' / 'y' / '1' = True
    # -- 'false' / 'f' / 'no' / 'n' / '0' = False
    if isinstance(expects, bool):
        answer = Validate.eval_boolean(answer)

    elif not isinstance(expects, str):
        # print(f"Return type requested: {expects}")
        try:
            answer = expects(answer)
        except ValueError as e:
            print(e)

    # print(f"Answer type: {type(answer)}")
    return answer


def get_categories():
    """Collect current categories from the OpenTriviaDB API,
    Returns a List of Category Objects"""
    response = requests.get('https://opentdb.com/api_category.php', timeout=5)
    # response.raise_for_status()
    if not response:
        raise requests.RequestException(response.status_code)

    cdata = response.json()
    trivia_categories = []
    for tc in cdata['trivia_categories']:
        cat_num, cat_name = tc.values()
        trivia_categories.append(TriviaCategory(cat_num, cat_name))

    return trivia_categories


def select_category(categories):
    """Allow user to select from the list of question categories"""
    lookup = []
    # Display all categories
    for i, cat in enumerate(categories, 1):
        lookup.append(cat.id)
        print(f"{i}. {cat.name}")
    # Workout the highest number that should be accepted
    highest = len(lookup) - 1
    # Ask player to select one category from the list
    choice = ask(
        expects=int,
        question="Please enter a category number: ",
        error_msg="Please enter a number from the list shown above!",
        validation=[
            Validate.as_integer,
            (Validate.is_less_than, highest)
        ],
    )
    return lookup[choice-1]  # <- account for enumeration offset!


def get_constant_name(value, cls):
    """Get the name of a Constant from it's value"""
    return [name for name, val in cls.__dict__.items() if val == value]


async def connect_client():
    """Create OpenTriviaDB Client instance,
    optionally request a token,
    Returns Client object (async)"""
    # We'll use the client via a context manager
    async with Client() as client:
        try:
            # Request a token for the game session (avoids repeat questions)
            await client.request_token()
        except RuntimeError:
            await client.reset_token()
        return client


async def quiz_round(game, q_num, q_cat, q_diff, q_type):
    """Uses the OpenTriviaDB Client object (game) to run a round of Questions"""
    # Round variables:
    current_score = 0
    current_question = 0

    async for q in game.round(
        amount=q_num,
        category=q_cat,
        difficulty=q_diff,
        type=q_type,
    ):  # <- NOTE: Yields `Question` objects.
        current_question += 1
        given_answer = ask(
            f"Q{current_question}. {q.question} ",
            validation=Validate.as_boolean,
            expects=bool,
        )
        print(f"Given answer: {given_answer}")
        if str(given_answer).lower() == q.correct_answer.lower():
            current_score += 1
            print("You got it right!")
        else:
            print("Sorry, that's incorrect.")

        print(f"The correct answer is: {q.correct_answer}")
        print(
            f"Your current score is: "
            f"{current_score}/{current_question}\n"
        )

    return (current_score, current_question)


async def quiz_game():
    """Run the Quiz Game using the OpenTriviaDB API Client"""
    # API options:
    number_of_questions = 10
    question_category = 9
    question_difficulty = "easy"
    question_type = "boolean"

    # Game variables:
    current_round = 1
    round_score = 0
    round_questions = 0
    total_score = 0
    total_questions = 0

    # Game loop:
    while current_round <= number_of_rounds:
        if ask(
            "Would you like to choose a category for this round? [y/n] ",
            expects=bool,
        ):
            question_category = select_category(all_categories)
            category_name = Category(question_category)

        q_type = ""
        if question_type == "multiple":
            q_type = question_type + " choice "
        if question_type == "boolean":
            q_type = "True/False "

        print(f"Category name: {category_name}")
        category_name = str(question_category[8:]).capitalize()
        print(f"Category value: {question_category}")

        print(f"Round {current_round}...")
        print(f"This will consist of {number_of_questions} "
              f"{question_difficulty}, {q_type}questions of "
              f"{category_name}.\n"
              )

        async with Client() as client:
            # Request a token for the game session (avoids repeat questions)
            await client.request_token()

            # if not isinstance(question_category, Category):
            #    question_category = Category(question_category)

            try:
                round_score, round_questions = quiz_round(client,
                                                          number_of_questions,
                                                          question_category,
                                                          question_difficulty,
                                                          question_type
                                                          )

            except TokenNotFound:
                await client.request_token()

            except TokenEmpty:
                print(
                    "Exhausted available questions for the specified options!"
                )
                if ask(
                    expects=bool,
                    question="Reset the session and continue?"
                             "(Questions will repeat!) [y/n] ",
                    error_msg="Please enter 'y' or 'n'...",
                    validation=(Validate.as_boolean)
                ):
                    # Reset the session token
                    client.reset_token()

            except NoResults:
                print(
                    "Sorry, there are not enough questions to fulfil "
                    "your request"
                )

        total_score += round_score
        total_questions += round_questions
        current_round += 1

    # Final score etc.
    print("You finished the quiz")
    print(f"Your final score is: {total_score} out of {total_questions}")


# Pre-Game set up:
all_categories = get_categories()
number_of_rounds = ask(
    expects=int,
    question="How many rounds would you like to play? ",
    error_msg=E_PROMPT + ": Please enter a numerical character...",
    validation=[Validate.as_integer, Validate.is_greater_than_zero]
)

asyncio.run(quiz_game())
