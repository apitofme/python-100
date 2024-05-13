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
