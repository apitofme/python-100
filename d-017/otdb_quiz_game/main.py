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

# Game options:
MAX_ROUNDS = 5
MAX_QUESTIONS = 20
VALIDATION_ERROR = "Invalid response!"

# API options:
DIFFICULTY_OPTIONS = ["easy", "medium", "hard"]
TYPE_OPTIONS = ["boolean", "multiple"]

# Default values:
DEFAULT_AMOUNT = 10
DEFAULT_CATEGORY = 9  # <- General Knowledge
DEFAULT_DIFFICULTY = "easy"
DEFAULT_TYPE = "boolean"


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

    @staticmethod
    def in_values(value, values: list):
        """Returns True if value is in the list of values, False otherwise"""
        return value in values


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


def ask(question, error_msg=VALIDATION_ERROR, validation=None, expects=str):
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
    if expects == bool:
        # print("Interpreting answer as boolean...")
        answer = Validate.eval_boolean(answer)

    elif expects != str:
        # print(f"Return type requested: {expects}")
        try:
            answer = expects(answer)
        except ValueError as e:
            print(e)

    # print(f"Answer {answer}, Type: {type(answer)}")
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
    if ask(
        "Would you like to choose a category for this round? [y/n] ",
        expects=bool,
    ):
        lookup = []
        # Display all categories
        for i, cat in enumerate(categories, 1):
            lookup.append(cat.id)
            print(f"{i}. {cat.name}")

        # Ask player to select one category from the list
        choice = ask(
            expects=int,
            question="Please enter a category number: ",
            error_msg="Please enter a number from the list shown above!",
            validation=[
                Validate.as_integer,
                (Validate.is_less_than, len(lookup) - 1)
            ],
        )
        # print(f"FNC: select_category -- returned choice = {choice}")
        return lookup[choice-1]  # <- account for enumeration offset!
    return False


def select_type():
    """Allow user to select the type of question"""
    if ask(
        "Do you want to choose the type of questions for this round? [y/n] ",
        expects=bool,
    ):
        # NOTE: May need to handle more types in the future!
        choice = ask(
            "Please enter either 'T' for True/False, "
            "or 'M' for Multiple Choice: ",
            validation=(Validate.in_values, {'values': ['t', 'm']})
        )  # NOTE: user input via 'ask' ALWAYS uses .lower()!
        # print(f"FNC: select_type -- returned choice = {choice}")
        if choice == 't':
            return "boolean"
        if choice == 'm':
            return "multiple"
    return False


def select_difficulty():
    """Allow user to select the question difficulty level"""
    if ask(
        "Do you want to choose a difficulty for the questions this round? "
        "[y/n] ",
        expects=bool,
    ):
        choice = ask(
            "Please enter [E]asy, [M]edium or [H]ard: ",
            validation=(
                Validate.in_values,
                {'values': ['e', 'm', 'h', 'easy', 'medium', 'hard']}
            )
        )  # NOTE: user input via 'ask' ALWAYS uses .lower()!
        if choice == 'e':
            return "easy"
        if choice == 'm':
            return "meduim"
        if choice == 'h':
            return "hard"
        return choice
    return False


def select_amount():
    """Allow user to select the number of questions for the round"""
    if ask(
        "Do you want to choose how many questions for this round? ",
        expects=bool,
    ):
        return ask(
            "How many questions do you want this round? [MAX=20] ",
            validation=(Validate.is_less_than, MAX_QUESTIONS),
            expects=int
        )
    return False


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
    # Game variables:
    current_round = 1
    round_score = 0
    round_questions = 0
    total_score = 0
    total_questions = 0

    # Game loop:
    while current_round <= number_of_rounds:
        # Select question category:
        qc = (
            select_category(all_categories)
            or DEFAULT_CATEGORY
        )
        question_category = Category(qc)
        # Get the category name from the constants in the Category class
        category_name = question_category.name.replace("_", " ").title()

        print(f"Category value: {question_category}")
        print(f"Category name: {category_name}")

        # Select question type:
        question_type = select_type() or DEFAULT_TYPE
        type_name = ""
        if question_type == "multiple":
            type_name = question_type + " choice "
        if question_type == "boolean":
            type_name = "True/False "

        # Select question difficulty:
        question_difficulty = select_difficulty() or DEFAULT_DIFFICULTY

        # Select question amount:
        question_amount = select_amount() or DEFAULT_AMOUNT

        # Display round header:
        print(f"Round {current_round}...")
        print(f"This will consist of {question_amount} "
              f"{question_difficulty}, {type_name}questions "
              f"in {category_name}.\n"
              )

        async with Client() as client:
            # Request a token for the game session (avoids repeat questions)
            await client.request_token()

            # if not isinstance(question_category, Category):
            #    question_category = Category(question_category)

            try:
                round_score, round_questions = (
                    await quiz_round(
                        client,
                        question_amount,
                        question_category,
                        question_difficulty,
                        question_type
                    )
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
    error_msg=VALIDATION_ERROR + ": Please enter a numerical character...",
    validation=[Validate.as_integer, Validate.is_greater_than_zero]
)

asyncio.run(quiz_game())
