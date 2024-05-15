"""
-=< 100 Days of Python >=-
-=[ Day 005 ]=-
"""
"""
L.51 - Using the 'for' loop with Lists

>> What is a 'for' loop?

In programming a loop defines a block a code that we want to run over and
over again. Typically we want to do this for a given number of times, or
for each piece of data in a given data-set (e.g. FOR every Item in a List).

While other types of loops do exist, the first and most useful that we'll
introduce is the 'for' loop. This works almost exactly as our pseudo-code
example above, using the 'for' keyword followed by a name we want to use
to represent the individual Item within thee loop, then the 'in' keyword
followed by the name of the iterable object we want to loop over/through.
"""
# create a list
fruits = ["Apple", "Peach", "Pear"]
# loop through the list to print out each item
for fruit in fruits:
    print(fruit)
"""
When we run this code each individual Item ('fruit') from the List
('fruits') is printed out using the 'print()' function. Since there are
three items in the list the 'print()' function gets called three times,
once for each Item, so there are three separate lines printed out.

We can think of the word 'fruit' we give as being the variable name used
to represent the Item on each iteration through the loop, the associated
value being updated each time so that it always represents the current
Item. The 'for' loop will automatically terminate when there are no more
items in the list.

Note that we are not limited to running a single line but rather we can
define a whole block of code that will be executed on each cycle through
the loop. This can contain any valid Python code, such as conditional
statements and even other loops.

Everything indented beneath the 'for' statement (after the colon ':') is
"inside" the loop and will be executed on each cycle through. Anything
following the loop that is not indented is considered "outside" the loop
and will run as normal (i.e. once).
"""
# let's space out our next example from the previous one
print("\n")

# a more complex example
for f in fruits:
    # everything at this indentation level is "inside" the loop!
    # a conditional statement
    if f[0] == 'P':
        print(f + " begins with a 'P'")
    else:
        print(f + " does NOT begin with a 'P'")

    # another conditional statement
    if len(f) > 4:
        print(f"Sorry but '{f}' is too long, I can't count above 4!")
    else:
        print(f + " has a short name, it's spelt...")
        # a loop within a loop
        for letter in f:
            print(letter)

    print("This is printed at the end of each loop!\n")
# un-indented code is "outside" of the loop, so only runs once
print("This is printed only once, after the loop has finished!")

"""
L.52 - Coding Exercise: Average Height
"""
# See external file: "exercise_average_height.py"

"""
L.53 - Coding Exercise: High Score
"""
# See external file: "exercise_high_score.py"

"""
L.54 - Using 'for' loops with the 'range()' function
Ref: https://docs.python.org/3.12/library/stdtypes.html#typesseq-range

NOTE: "Rather than being a function, range is actually an immutable sequence type..."

We won't always want to use a 'for' loop with a List, sometimes we just
want to be able to loop over some code a given number of times. In this
case we can use the 'range()' function to produce a series of integers
for the loop, acting as a kind of loop-counter.

Range is defined with up to 3 parameters: 'start', 'stop' and 'step'
Where:  "If the step argument is omitted, it defaults to 1.
        If the start argument is omitted, it defaults to 0."

Let's take a look at an example:
"""
for number in range(1, 10):
    print(number)
# => 1 2 3 4 5 6 7 8 9
"""
Note that this prints out every number from (including) "1" up to but NOT
including "10"! - If we want to include '10' then we actually have to set
the upper-bound ('stop') parameter to "11".

Let's take a look at what happens if we add a 'step' parameter...
"""
for number in range(1, 11, 3):
    print(number)
# => 1 4 7 10
"""
Notice that this time the gap ('step' size) between each number is "3",
so the output jumps from "1" (+3) to "4" then (+3) to "7" and finally
(+3) to "10".


>> Real world problem:

When Carl Gauss (the historic German mathematician) was just a child his
maths teacher gave him an exercise where he was asked to add all of the
numbers from 1 to 100 -- presumably to keep him busy for a while. However,
much to his teachers surprise, it was only a few minutes before he came
back to her with the answer.

So how did he do it?
Well as a bright kid he realised that if he inverted the sequence of
numbers beneath the original sequence (imagine folding it in half
back on itself) he had a problem that looked like this...

    1   2   3   4   5   ...
    100 99  98  97  96  ...

With this it became clear the sum at each step added up to 101 (1+100,
2+99, 3+98 etc.) which left him with 50 instances of 101 to add up:

    50 x 101 = 5050

Now we might not be prodigal mathematicians, but as programmers we can
actually solve this problem even faster than Gauss with just a few lines
of code...
"""
total = 0
for number in range(1, 101):
    total += number
print(total)  # => 5050

"""
L.55 - Coding Exercise: Adding Even Numbers
"""
# See external file: "exercise_add_even.py"

"""
L.56 - Coding Exercise: FizzBuzz (Job Interview Question)
"""
# See external file: "exercise_fizz_buzz.py"
