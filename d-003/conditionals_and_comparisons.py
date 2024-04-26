"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-
"""
"""
L.30 - Control Flow with Conditional Statements:

Conditional statements basically allow us to ask questions in our code
and perform different operations (i.e. run different code) based on
the answer.

So with the "IF...ELSE" statement we can test for a specific condition
then run some code [IF] the statement is 'true', or [ELSE] we run some
different code when the test condition is 'false'.

For example:
"""
# Note: the single '=' sign here denotes "assignment"
#       (i.e. variable _equals_ value)
test_condition = True

if test_condition:
    print("Test 1: The test condition is 'true'\n")
else:
    print("Test 1: The test condition is NOT true (i.e. is 'false'!)\n")
# notice how only the first statement under IF gets run!

# See if you understand the following example:
if test_condition == False:
    print("Test 2: The test condition is 'true'\n")
else:
    print("Test 2: The test condition is NOT true (i.e. is 'false'!)\n")
"""
This time we tested the variable's value against another value using
what's called a 'conditional operator', in this case we were testing
for 'equality' (i.e. does THIS _equal_ THAT).

Since we know the value stored in the 'test_condition' variable is TRUE,
but we are asking if that is equal to FALSE, we can see how the answer is
no (not 'true'): since TRUE does not equal FALSE. So this time the code
indented under the ELSE part of the conditional statement is what gets
executed, since the condition wasn't met to run the first part.

We can also begin to see how, depending on the 'question' being asked
in the conditional statement, IF/ELSE does not have to represent direct
opposite values, instead 'else' can be thought of as the "catch-all".
Whenever a test-value does not meet the conditional criteria the code
in the ELSE block is what will be run.
"""
"""
- Comparison Operators:

There are several basic comparison operators we can use in our
conditional test, allowing us to test for different conditions
-- it doesn't always have to be "does THIS _equal_ THAT" ...

    Operator        Meaning
    --------        -------
        >           Greater than
        <           Less than
        >=          Greate than or equal to
        <=          Less than or equal to
        ==          Equal to
        !=          Not equal to

"""
number = 10

if number > 10:
    print("The test number is greater than 10")
else:
    print("The test number is NOT greater than 10")
# notice the output from this test may not be what you were expecting!

# let's fix that here:
if number >= 10:
    print("The test number is greater or equal to 10")
else:
    print("The test number is less than 10")

"""
L.31 - Coding Exercise: Introducing the Modulo
"""
# See external file: "exercise_TODO.py"

"""
L.32 - Introducing additional test statements with ELIF:

We can demostrate some of the quirks of these operators by introducing
another part of these conditional statements, the "ELIF" (i.e. 'else-if').
An ELIF block allows us to chain additional conditional tests together
within the same contextual block of code.

Effectively we are adding additional 'questions' or tests to consider.
Where each additional test is only checked if the answer to the previous
was NOT true, and only proceeding to the ELSE when ALL test are false!

Now we can split the example from before to show different cases:
"""
number = 10
# This time however we'll change the first test condition to 9!
if number > 9:
    print("The test number is greater than 10")
elif number >= 10:
    print("The test number is greater or equal to 10")
else:
    print("The test number is less than 10")
"""
Note that it still only prints one output, the one from the first statement
that is 'true'!

It does NOT run the code from ALL statement blocks that equate to true
because once a test passes all other sections are ignored, and if no
tests pass then only the 'else' code-block is run.

The entire [IF...ELIF...ELSE...] section is regarded as a single, cohesive
statement. Whilst each sub-section has it's own indented block of code,
together they form a single conditional statement!

Try changing the value of 'number' and re-run the code to compare results.
"""
"""
- Nesting conditional statements:

Another thing that we can do with conditional statements is to 'nest' them
inside one another. This allows us to test for supplemental cases rather
than alternative cases ... what do we mean by that?

Well remember that a conditional statement is like asking a question.
So a nested statement is like a follow up question that is based on the
answer to the first question. Whereas an ELIF is more like an alternative
question, or alternative test conditions to consider if the first 'fails'.

Let's take an example of a roller-coaster at a theme park:
- you have to be over a certain height (e.g. 120cm) to ride
- but also there are different ticket prices depending on age
"""
height = int(input("How tall are you (in cm)?\n"))
if height >= 120:
    print("You can ride the roller-coaster...")
    age = int(input("How old are you?\n"))
    if age <= 12:
        # age is 12 and under
        print("It'll cost you $5")
    elif age < 18:
        # age is between 12 and 18 (i.e. under 18!)
        print("It'll cost you $8")
    else:
        # (everything else) age is 18 and over
        print("It'll cost you $12")
else:
    print("Sorry you aren't tall enough to ride this roller-coaster!")

"""
L.33 - Coding Exercise: BMI v2.0
"""
# See external file: "exercise_TODO.py"

"""
L.34 - Coding Exercise: Leap Year
"""
# See external file: "exercise_TODO.py"

"""
L.36 - Coding Exercise: Pizza Order
"""
# See external file: "exercise_pizza_order.py"
# - "exercise_pizza_alternative.py" has an alternative solution!

"""
L.37 - Logical Operators:

In addition to the basic comparison operators we saw before there are
also some basic 'logical' operators which further add to the set of
conditional tests we can create, these are:

        'and'       condition_a AND condition_b
        'or'        condition_a OR condition_b
        'not'       is NOT condition_a
        
So for 'and' we can say that a conditional test using this logical operator
will ONLY return 'true' if BOTH conditions are met, A and B. If either test
equates to 'false' then the whole statement becomes FALSE.
    - e.g. - IF has_apple AND has_pear ...
    So if I only have a pear the combined statement equates to 'false'!
    I would need to have an apple also for the overall test condition to
    be 'true'.

Hopefully from that it should already be clear now what will happen if we
use the 'or' operator - only one of the conditions needs to be 'true':
    - IF has_apple OR has_pear ...
    Now even with only a pear the combined statement equates to 'true'!

The 'not' operator is used to test for the opposite of a statement's result.
So if a statement equates to 'true' then using 'not' would make the result
'false'. It may seem hard to understand why or when we might need this but
it will become apparrent, especially when we get to 'while' statements!
"""

"""
L.38 - Coding Exercise: Love Calculator
"""
# See external file: "exercise_TODO.py"
