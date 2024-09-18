"""
-=< 100 Days of Python >=-
-=[ Day 012 ]=-
"""

"""
NOTE: The course has been updated! - 5th Aug 2024
The course was updated (and presumably reorganised), which has resulted in
the lesson numbers changing. So although previously we had reached lesson
#100 on Day 10, picking up the course again after a break over the summer,
we now find ourselves here on Day 12 at lesson #87!

The update was largely due to the constraints and issues caused by reliance
on 3rd-party services (such as "repl.it"). In an effort to move away from
these services, the course was refactored to encourage using the JetBrains
"PyCharm" IDE from the get-go.
"""
# >> Pylint clean-up for this file
# pylint: disable=redefined-outer-name,global-statement
"""
L.87 - Namespaces: Local vs Global

>> NAMESPACE:
Namespaces are how the Python interpreter keeps track of, and logically
groups together, all the different named entities (such as variables and
functions) within our code. Effectively it ensures that each named-entity
is uniquely identifiable, whilst encapsulating the entity within an
applicable context of code to which it is relevant. This is done so that
the interpreter can guarantee each entity's availability and persistence
is maintained for as long as it is required during code execution, and so
that the computer's resources can be efficiently managed at run-time.

>> SCOPE:
Scope can be thought of as the "context" in which a given named-entity is
relevant. Essentially the 'scope' refers to the areas within our code that
different named entities are available.

-   'Global' is the outermost scope. Entities defined in this context are
    (theoretically) available to all other parts of your code.

-   'Local' is the innermost scope, relative to the current position of
    code execution. Entities defined here are only available to code within
    same code-block, or (potentially) sub-blocks.


Consider the following code...
"""
number = 1


def update_number():
    """Redefine the value of a variable (demonstrating 'scope')"""
    number = 2
    print(f"Number inside function: {number}")


update_number()
print(f"Number outside function: {number}")

"""
What do you expect the output of each print statement to be?

Results:
"Number inside function: 2"
"Number outside function: 1"

...but why?

This is because Python actually interprets the two assignments to the name
'number' as separate entities due to Namespace scoping. We assigned the new
value '2' inside a function, but functions create a new local-scope that
applies only within the context of code inside that specific function.
"""

"""
L.88 - Does Python have Block Scope?

The short answer is no!

Block scope applies to any 'block-level' code, demarcated by indenting in
Python or by special delimiter characters in other languages (such as '{}'
or curly-braces in C and "C-Type" languages). In other languages it is
possible to define variables within a block-code and that variable with be
scope-limited to that block, Python however does not follow this convention.
In Python, any variable defined inside a block-statement (e.g. IF statements,
FOR and WHILE loops) will have the same scope as that of it's enclosing block.
"""
# For example:
a = 3
b = 2
if a > b:
    a_variable = 10

# 'a_variable' is still available at the global scope
print(a_variable)
# if it wasn't then the print statement would fail with an error
# since the variable name would be undefined in the global scope

"""
Coding Exercise 11: Prime Number Checker

Prime numbers are numbers that can only be cleanly divided by themselves
and 1.

Write a function that checks whether the number passed into it is a prime
number or not. -- It should return True or False.

e.g.
- 7 is a primer number because it is only divisible by 1 and itself.
- But 4 is not a prime number because you can divide it by 1, 2 or 4.

NOTE: 2 is a prime number because it's only divisible by 1 and itself,
but 1 is not a prime number because it is only divisible by 1.

Example Input     Example Output
    73                  True
    75                  False
"""


def is_prime(num):
    """Determine if a given number is 'prime' or not. Returns a Boolean"""
    prime = True
    if num > 2 and num % 2 == 0:
        # print(f"The number {num} is divisible by 2")
        prime = False
    else:
        base = (num // 2) + 1
        for n in range(2, base):
            # print(f"Dividing by {n}...")
            if num % n == 0:
                # print(f"The number {num} is divisible by {n}")
                prime = False
                break

    return prime


"""
L.89 - How to modify a Global Variable

We can reference values from an outer scope within the local scope of a
function by using special keywords:
-   'global' allows us to reference a global variable
-   'nonlocal' allows us to reference an outer-variable from inside a
    nested function

Now we can update the example to modify the global variable...
"""
# global scope
number = 1
print(f"Number initial value: {number}")


def reassign_number():
    """Reassign the value of a global variable within a local scope"""
    # use keyword to reference the global scope
    global number
    number = 2
    print(f"Number assigned inside function: {number}")


reassign_number()
print(f"Number outside function: {number}")

"""
However we cannot reference an entity created within a function's inner
scope at an outer level. In order to do this we would have to explicitly
pass the value back using the 'return' keyword, thereby creating a
reference assignment at the outer scope.

It is actually generally advised to avoid using global references all
together, unless absolutely necessary. Even then this is typically reserved
for the use of 'constants'!

So again, to avoid using the global reference within our function's local
scope we can use a 'return' statement, but to do so we must also add a
parameter in order to pass the global value in to the local-scope of our
function.

Let's implement this improvement now...
"""
# global scope
number = 1
print(f"Number initial value: {number}")


def increase_number(num):
    """Increase the value of a passed-in variable and return the updated value"""
    local_number = num + 1
    print(f"Local Number inside function: {local_number}")
    return local_number


# create the new assignment in the global scope
# using the function to increase the stored value
number = increase_number(number)
print(f"Number result of function: {number}")

"""
In practice it is preferable to use unique names for each entity, to avoid
any possible confusion and ensure the program is understandable to someone
else reading the code. So if we have a variable named 'counter' in the
global-scope, but want a similar variable within a function, we should alter
the name we use to something which identifies that specific entity (e.g. to
'function_counter') -- This is in effect what the Python interpreter does
internally, creating a unique scoped reference for each named entity to
prevent these kinds of accidental "name collisions", but a good programmer
should not rely on this in case of unexpected behaviour!
"""

"""
L.90 - Python Constants and the Global Scope

A constant by definition has a value which never changes (e.g. Pi).

When we want to define a constant in Python, technically, we have to use a
"variable". Even though the intention is that the value is never changed,
i.e. the variable name is never reassigned. Since Python puts the trust in
the programmer/user to 'behave' and act responsibly there is a convention
for naming constants in order to identify them as such, and that is to put
the name in ALL_CAPS.

The idea being that when we then want to reference one of these constants
inside a scoped function the CAPS_NAME reminds us that we shouldn't alter
or reassign the value in any way.
"""
