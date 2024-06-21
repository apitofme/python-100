"""
-=< 100 Days of Python >=-
-=[ Day 010 ]=-

Project: Calculator

Today's project is a classic and something that almost every programmer has
coded at some point, a Calculator program. Ours will be a simple text-based
program, taking one input at a time form the User and performing the chosen
operation to return the output, then allowing them to carry on with another
operation or giving them the option to clear the total and start again.

Rounding out our knowledge of functions, today in particular we'll focus on:
- Functions with Outputs;
"""
# import sys
from os import system

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

# Service Functions >>


def clear_terminal():
    """cross-platform way to clear the terminal screen"""
    system("cls||clear")


def refresh_display():
    """clear the terminal screen and (re)print the logo"""
    clear_terminal()
    print(logo)


def get_numeric_input(prompt, default=None):
    """function to obtain numerical user input with minimal validation
    NOTE: no type conversion is performed by this function, it simply
    asserts that a user input "is numeric" -- i.e. via `str.isnumeric()`
    """
    if default and not str(default).isnumeric():
        raise TypeError(
            'Parameter "default" MUST be numeric or a numeric string: ' +
            f'"{default}"'
        )

    user_input = None
    while not user_input or not str(user_input).isnumeric():
        user_input = input(prompt)
        if user_input.strip() == "" and default is not None:
            user_input = default
            break

    return user_input


def get_user_input(prompt, accepted_values, default=None):
    """generic function to obtain user input with minimal validation"""
    if default:
        default = str(default)
        if default not in accepted_values:
            raise ValueError("Default value NOT in accepted values!")

    user_input = None
    while str(user_input) not in accepted_values:
        user_input = input(prompt)
        if user_input.strip() == "" and default is not None:
            user_input = default
            break

    return user_input


def convert_numeric(s):
    """Converts a given numeric string to a suitable number format"""
    number = float(s)
    return int(number) if number.is_integer() else number


# Mathematical Functions >>

def multiply(multiplicand, multiplier):
    """Multiply two numbers ('factors') together and return the 'product'.
    - https://en.wikipedia.org/wiki/Multiplication
    """
    return convert_numeric(multiplier * multiplicand)


def divide(dividend, divisor):
    """Divide one number by another (the 'dividend' BY the 'divisor')
    returning the 'quotient'.
    - https://en.wikipedia.org/wiki/Division_(mathematics)
    """
    return convert_numeric(dividend / divisor)


def add(summand, addend):
    """Add two numbers together and return their 'sum'.
    - https://en.wikipedia.org/wiki/Addition
    """
    return convert_numeric(summand + addend)


def subtract(minuend, subtrahend):
    """Subtract one number from another (the 'subtrahend' FROM the 'minuend')
    returning the 'difference'.
    - https://en.wikipedia.org/wiki/Subtraction
    """
    return convert_numeric(minuend - subtrahend)


def power(base, exponent):
    """Raise a number (base) to an exponent and return the power).
    - https://en.wikipedia.org/wiki/Exponentiation
    """
    return convert_numeric(base ** exponent)


def root(radicand, degree):
    """Find the nth (degree) of a number (radicand) and return the root.
    - https://en.wikipedia.org/wiki/Nth_root#Complex_roots

    NOTE: This operation is uses "fractional exponentiation" to find the root
    (i.e. inverse of power by converting the exponent to a fraction). However
    this is NOT as precise as module specific functions - e.g. `math.sqrt()`!
    """
    return convert_numeric(radicand ** (1/degree))


# Definitions >>
# NOTE: Store the Function names as VALUES; User input provides the KEY;
#       This allows us to easily reference and call the required Function!
operations = {
    '*': multiply,
    '/': divide,
    '+': add,
    '-': subtract,
    'p': power,
    'r': root,
}
op_symbols = list(operations.keys())
running_total = None
# math_stream = []

while True:
    refresh_display()

    # first_number = running_total if running_total else convert_numeric(
    #    get_numeric_input("Please enter the first number: ")
    # )

    # Get the first number
    if running_total:
        first_number = running_total
        print(f"Current total: {running_total}")
    else:
        first_number = convert_numeric(
            get_numeric_input("Please enter the first number: ")
        )
        # math_stream.append(first_number)

    # Ask what operation to perform
    op_prompt = f"Please select an operation {op_symbols}: "
    operation = get_user_input(op_prompt, op_symbols)
    # math_stream.append(operation)

    # Ask for the second number
    second_number = convert_numeric(
        get_numeric_input("Please enter a number: ")
    )
    # math_stream.append(second_number)

    # Perform the requested operation
    running_total = operations[operation](first_number, second_number)

    # show calculation and current total
    print(f"{first_number} {operation} {second_number} = {running_total}")

    # Ask for next action
    ap = "Type 'c' to Continue, 'n' to start a New calculation or 'x' to Exit: "
    action = get_user_input(ap, "cnx")
    # print(f"Debug: {action}")

    # Action: New Calculation (i.e. clear the totals etc.)
    if action == 'n':
        print("New Calculation")
        running_total = None
        # math_stream = []

    # Action: Exit (i.e. end the program session / just break out of the Loop!)
    if action == 'x':
        print("Exiting")
        break

    # Action: Continue (loop through again, so update running total)
    # implied 'continue' since loop will automatically run again anyway!
