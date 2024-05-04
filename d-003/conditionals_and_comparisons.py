"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-
"""
"""
L.30 - Control Flow with Conditional Statements:

Conditional statements effectively allow us to ask simple 'truthy'
questions with our code and perform operations based on the answer.
Bascially we test for the 'truth' of a statement (the test-condition),
then perform actions based on the outcome of that test.

The first of these we will look at is the "IF...ELSE" statement...

>> IF ... ELSE:
The "if / else" conditional statement allows us to run one block of code
'IF' the test-condition is "True", or (optionally) a different block of
code (i.e. the 'ELSE' clause) when the test-condition is NOT "True"
(i.e. "False").

This can be thought of as:
-- if THIS ... else THAT
-- OR --
-- if THIS do something, ELSE do something else

For example:
"""
test_condition = True

print("Test 1:")
if test_condition:
    print("- The test condition is 'true'\n")
else:
    print("- The test condition is NOT 'true'\n")
# notice that only the statement indented under the 'IF' clause gets run!

# Now, see if you understand the following example:
print("Test 2:")
if test_condition == False:
    print("- The test condition is 'true'\n")
else:
    print("- The test condition is NOT 'true'\n")
"""
In the second test we compared the variable's value against another
value using what's called a 'comparison operator'. In this case we're
testing for "equality" (i.e. does THIS equal THAT), which we do using
a double equals sign -- Note: this is different from variable assignment
which only uses a sinlge equals sign to assign a value to a variable name!

Since we know the value stored in the 'test_condition' variable is TRUE,
our conditional statement equates to asking:

    if TRUE is equal to FALSE ...

The answer of course is "no" (i.e. the statement is NOT 'true'), therefore
the code indented under the 'ELSE' part of the conditional statement is
executed. (In other words the 'THAT' part of "if THIS ... else THAT")

It is also important to realise that, depending on the 'question' being
asked (i.e. what test-condition we use), IF and ELSE do not have to
represent directly opposing values (such as "True" and "Flase"). Instead
'else' can be thought of as the "catch-all" statement, so that whenever
a test-value does NOT equate to "True" (for the given test-condition) then
the code in the 'else' block is executed.

Being able to execute different blocks of code in this way, when different
inputs are given or different conditions arise, is what is known as
"flow control" (because we control the 'flow' of our program). This will
allow us to write more powerful and versatile applications as we progress.

There are other times we will make use of conditional statements beyond
the "if ... else" format, but we will get to those later. For now let's
have a look at the different types of comparisons we can perform to allow
us to write different test-conditions...
"""
"""
>> Comparison Operators:

There are several basic comparison operators we can use in our
conditional tests, allowing us to test for different conditions
-- it doesn't always have to be "does THIS equal THAT" ...

    Operator        Meaning
    --------        -------
        >           Greater than
        <           Less than
        >=          Greate than or equal to
        <=          Less than or equal to
        ==          Equal to
        !=          Not equal to

Let's have a quick look at some examples to demonstrate how some of these
comparison operators work:
"""
# First let's create a variable to test, giving it the numerical value 10
number = 10

# Now we can compare that variable to another value:
# - here we'll use the "greater than" symbol '>'
# -- effectively asking: "if 10 is greater than 10"
if number > 10:
    print("The test number is greater than 10")
else:
    print("The test number is NOT greater than 10")
# Notice the output from this test may not be what you were expecting!
# It ran the code block under the 'else' clause, but why? ...
# It's because 10 is not GREATER than 10 (i.e. it is not MORE than 10)
# To include 10 we shouild use the "greater than or equal to" operator
if number >= 10:
    print("The test number is greater or equal to 10")
else:
    print("The test number is less than 10")
# Now we should see the output from the 'if' code block!

"""
L.31 - Coding Exercise: Odd or Even (Introducing the Modulo)
"""
# See external file: "exercise_odd_or_even.py"

"""
L.32 - Introducing the ELIF:

The final (optional) component of these "if...else" statements we'll look
at is the "elif" ('else if'), which allows us to use and chain additional
conditional tests after the intitial 'if' statement.

Effectively we are adding additional 'questions' or tests to consider,
where each additional test is only checked if the 'answer' to the previous
was NOT true (i.e. false), and only proceeding to the 'else' when ALL
previous 'if' or 'elif' tests return false!
-- i.e. "if (not) THIS ... or THIS ... or THIS ... then THAT"

...and we can chain as many together, one after another as we need.

Let's update the example from before to show different cases:
"""
number = 10
# This time however we'll change the first test condition to "> 9"
if number > 9:
    print("The test number is greater than 10")
elif number >= 10:
    print("The test number is greater or equal to 10")
else:
    print("The test number is less than 10")
"""
Note that although both of the conditional test are technically 'true',
since '10' is both "greater than 9" and "greater than or equal to 10",
we still only see one output printed (i.e. the first one). This is because
not all test are evaluated. Processing the statements in order, the first
test to pass as 'true' will have it's code-block executed, the rest of the
conditional statement is ignored -- remember it is

    "if 'this' ... OR 'this' ... OR(else) 'that'"

This means that only if the previous test was 'false' is the next test
considered, and only the first test to pass has it's indented code run.
After which the entire conditional statement, from the 'if' to the end of
the 'else' block is considered completed. Each block represents an option
but it is NOT multiple-choice, once one is true all others are ignored.
-- It's almost like a Schroedinger's Box of code, there are many
possibilities but once we open it (i.e. run the code) only one remains!

... and if no tests pass then only the 'else' code-block is run.

The entire [IF...ELIF...ELSE...] section is regarded as a single, cohesive
statement. So whilst each sub-section has it's own indented block of code,
together they form a single conditional statement!

Try changing the value of 'number' and re-run the code to compare results.
"""
"""
>> Nesting conditional statements:

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
# See external file: "exercise_bmi_v2.py"

"""
L.34 - Coding Exercise: Leap Year
"""
# See external file: "exercise_leap_year.py"

"""
L.35 - Multiple IF statements:

When we use an 'elif' in a conditional statement we are only ever going
to satisfy one test-condition, even if we check for multiple conditions,
and consequently only one code-block will be run.

However, what if we want to test for multiple conditions that might ALL
be true, and we want to run some code for each condition that IS true
regardless of the outcome of any of the other tests? Well, that is where
multiple 'if' statements comes in.

Since each 'if' statement has it's own test condition and indented
code-block we can simply have multiple separate statemnts. Each one
test's for a condition and runs it's code-block if that condition is met.
Remember an 'if' does NOT require an 'elif' or 'else' to be present, so
we don't have to include an 'else' clause when the alternative action for
a given test is simply "do nothing". Also, since we're not 'nesting' any
of these separate statements, each is evaluated independent of the others.

For an example, imagine we were asked to write a simple program for a
hotdog vendor. They provide information about what questions they ask
their customers such as: "Do you want ketchup / mustard?"; "Do you want
onions?"; "Would you like a drink also?" etc. - These will be the basis
of our conditional tests.

However, if we wrote the code out using 'elif's then the customer could
only choose one and whichever one they said yes to first would be what
they'd get ... Let's demonstrate:
"""
# Assume that we've taken anwers to the questions as inputs, resulting in
wants_ketchup = True
wants_mustard = True
wants_onions = True
# We then process the order as follows:
hotdog = "Sausage in a bun"
if wants_ketchup:
    hotdog += " with red sauce"
elif wants_mustard:
    hotdog += " with yellow sauce"
elif wants_onions:
    hotdog += " with onions"
# Then 'give' the hotdog to the customer
print(hotdog)
"""
Notice that, as we learned with an 'if...elif' statement only the first
condition which is true has it's code-block executed, the others are
skipped. This means that our 'greedy' customer doesn't get all of the
toppings they want on their hotdog, they only get ketchup (red sauce)!

In order to allow each statement to be processed independently, thereby
allowing multiple conmditions to be true AND have their associated code
executed we must use separate 'if' statements...
"""
# Assuming the same inputs as before
hotdog = "Sausage in a bun"
if wants_ketchup:
    hotdog += " with red sauce"

if wants_mustard:
    hotdog += " with yellow sauce"

if wants_onions:
    hotdog += " with onions"

# and give the hotdog to the customer
print(hotdog)
"""
Now the output might be a bit 'messy' as far as being a good sentence,
but it conveys all the necessary information, and if the text were an
actual hotdog it would meet the customers order as specified!
"""

"""
L.36 - Coding Exercise: Pizza Order
"""
# See external file: "exercise_pizza_order.py"

"""
L.37 - Logical Operators:

In addition to the comparison operators we looked at before there is
also a set of 'logical' operators we can use in Python which allow us to
build up more complex conditional tests by combining multiple conditions
in different ways. These are:

    Keyword:        Format:
    --------        -------
    "and"           'condition_a'  AND  'condition_b'
    "or"            'condition_a'  OR  'condition_b'
    "not"           is  NOT  'condition'
        
So, when using "and" we can say that a conditional test will only return
'true' if BOTH conditions are met ('a' AND 'b'). If either condition is
'false' then the whole statement equates to "false".

    -- e.g:  IF  has_apple  AND  has_pear ...
    In this case if I only have a pear then the overall statement equates
    to "false". I would need to have an apple as well for the statement
    to be true!

Given that example you can probably imagine what will happen if we use
the "or" operator. This requires only one of the conditions to be 'true':

    -- IF  has_apple  OR  has_pear ...
    Now, even with only a pear the combined statement equates to "true"!

With "or" it is only if BOTH conditions are 'false' that the overall
statement equates to "false".

Lastly, the "not" operator is used to negate ('flip') the boolean value
of the given 'operand' (test condition). It inverts the logic of the
given condition or expression and returns the opposite value, e.g:

    - If a condition equates to 'true' then the "not" operator will make
    the statement return "False".
    - If the condition is 'false' then "not" will make the statement
    return "True"

You can use the "not" operator in various contexts, such as conditional
statements and while loops, and it's handy when you need to check for
unmet conditions or control the flow of execution in your programs.
Remember that the operand can be any Boolean expression or even a
user-defined value or object!

Example: (pseudo-code)

    if NOT "happy" then:
        Go outside, Go for a walk, Get some fresh air!
    else:
        Yay! I'm happy! =)
"""
r1 = 2 > 5  # 2 is greater than 5 => False
r2 = not 2 > 5  # NOT 2 greater than 5 (~"2 NOT greater than 5") => True
print(r1)
print(r2)
"""
BONUS Coding Exercise: Rollercoaster Ticket (Midlife-Crisis Edition)
"""
# See external file: "rollercoaster_midlife_crisis.py"

"""
L.38 - Coding Exercise: Love Calculator
"""
# See external file: "exercise_love_calculator.py"
