"""
-=< 100 Days of Python >=-
-=[ Day 006 ]=-
"""
"""
L.63 - While Loops
Ref: https://docs.python.org/3/reference/compound_stmts.html#while

The "while" statement is another kind of loop, similar to a "for" loop
except that instead of looping through FOR a given number of times it
loops WHILE a conditional statement remains TRUE -- i.e. the loop will
keep going UNTIL the test condition becomes FALSE.

Let's have a look at a simple example:
"""
loop_counter = 0
while loop_counter < 5:
    print(loop_counter)
    # we MUST remember to increment the loop counter each time
    loop_counter += 1
# This is effectively the same as: "for loop_counter in range(5)"
"""
You have no doubt heard of the term "infinite loop" as a much feared
programming error which can crash a program or computer. This is an
entirely possible situation we can get in to with 'while' loops if we
choose a test condition that will ALWAYS be 'true'. Therefore it is
important for us as programmers to choose an appropriate test condition,
and/or update it as needed inside the loop, to ensure that this doesn't
happen!

In other words, if we didn't have the line incrementing 'loop_counter' in
the example above then the test would ALWAYS be "True" because the counter
would NEVER change value (i.e. it will never NOT be less than 5). Meaning
if we actually ran it without that line it would continue looping forever,
never reaching an exit condition (theoretically). In practice of course
computers have their limits, so the program would only continue printing
output lines (of "0") until some sort of software or hardware limit was
reached (e.g. it runs out of memory and crashes) or we manually force the
program to stop by terminating the process.


>> Continue and Break

In addition to the loop statements there are a couple of other keywords
Python provides that we should know about when when working with loops.
The first of these is the "continue" statement, which automatically skips
ahead ('continues') to the NEXT cycle of the loop. It does so immediately,
ignoring any remaining code in the CURRENT cycle. Then there is the "break"
statement which allows us to break-out of a loop, ending the loop entirely
at that point. This too ignores any remaining code for the CURRENT cycle
and prevents any more cycles, continuing with code below/outside of the
loop if present.


>> Reeborg's World Challenge: "Hurdle 2"
- Jumping a Random Number of Hurdles

Let's return to the Reeborg's World website, this time selecting the
"Hurdle 2" option from the first drop-down menu.

World Info:
Reeborg has entered a hurdle race, but he does not know in advance how
long the race is. Make him run the course, following a path similar to
the one shown, but stopping at the only flag that will be shown after the
race has started.

What you need to know:
    - The functions move() and turn_left().
    - The condition at_goal() and its negation.
    - How to use a while loop.

Your program should also be valid for world "Hurdles 1".


The code panel on the right should have retained our previous solution to
the "Hurdle 1" problem, which includes any functions we defined such as
"turn_right". We can leave these here in order to use them again.

NOTE: If you want to you can move the function definitions in to the
      'Library' tab in the code panel to help keep the 'Python Code' tab
      clearer. In which case however, in order to use the functions you
      must first import them in to the 'Python Code' tab using the import
      statement -- e.g. "from library import jump"

We will also need to make use of a 'condition', which if you click on
"Reeborg's Keyboard" and select the "conditions" tab you will see a list
of all of the conditions available to us. The one we want is the first in
the list "at_goal()", which equates to "True" ONLY when Reeborg is at the
goal (finish-line flag). You will need to think about how to use this in
the WHILE loop in such a way that the loop continues until "at_goal()" is
"True" -- Remember the WHILE loop requires a 'true' condition which will
become 'false' to end the loop. This is the opposite of what the 'at_goal'
condition provides us, so we need to find a way to flip or negate it in
our test statement...


>> Solution:

NOTE: If you chose to leave the 'jump' function in the 'Python Code' tab
      then you don't need the import line!

    from library import jump
    while not at_goal():
        move()
        jump()

Remember that the "not" keyword works in conditional statements to flip
or negate the logical boolean value of an expression, so that 'True'
becomes 'False' and vice-versa.
Ref: https://docs.python.org/3/reference/expressions.html#not


However it's possible that you solved the problem like this:
    
    "while at_goal() == False"

If so that's absolutely fine and the code will still work to solve the
problem. You should be aware however that "== False" and "not (True)" are
not always the same thing in Python. Remember that a variable with almost
ANY value not explicitly "False" equates to "True" -- e.g. a non-empty List
or String, any non-zero integer or floating-point number ... etc.


>> While/For Art Though Loop

Sometimes it can be difficult to decide when to use a WHILE loop and
when to use a FOR loop, as often we could use either to achieve the
same thing.

Generally it is best to use a FOR loop when you know ahead of time how
many times you want the loop to run, or if you are using the loop to
iterate through a series of stored data-points such as a List -- i.e.
the length of the loop is predetermined.

The WHILE loop on the other hand is used when we want to loop an undefined
number of times, repeating the loop indefinitely until a certain condition
is changed -- e.g. until some user input tells the program to stop.
"""

"""
L.64 - Reeborg's World Challenge: "Hurdle 3"
- Jumping a Random Number of Hurdles in Random Positions

World Info:
Reeborg has entered a hurdle race. Make him run the course, following the
path shown.

The position and number of hurdles changes each time this world is reloaded.

What you need to know:
    - The functions move() and turn_left().
    - The conditions front_is_clear() or wall_in_front(), at_goal(), and
      their negation.
    - How to use a while loop and an if statement.

Your program should also be valid for worlds "Hurdles 1" and "Hurdles 2".


>> Solution:

    from library import jump
    while not at_goal():
        if wall_in_front():
            jump()
        else:
            move()

This time because the hurdles are in random positions we need to make use
of a second condition ("wall_in_front()") in order to tell Reeborg when to
'jump' -- i.e. IF there's a 'wall_in_front' (i.e. a 'hurdle') then jump it,
otherwise move forward.

...and because this conditional test is inside the the WHILE loop it will
run as many times as is needed, checking for a wall OR moving forwards each
time, until "not at_goal()" becomes False (i.e. 'at_goal' is True).
"""

"""
L.65 - Reeborg's World Challenge: "Hurdle 4"
- Jumping over Random Hurdles with Variable Heights

World Info:
Reeborg has entered a hurdle race. Make him run the course, following the
path shown.

The position, the height and the number of hurdles changes each time this
world is reloaded.

What you need to know:
    - You should be able to write programs that are valid for worlds
      "Around 4" and "Hurdles 3", and to combine them for this last
      hurdles race.

Your program should also be valid for worlds "Hurdles 1", "Hurdles 2" and
"Hurdles 3".


>> Solution:

    # possibly inside the "Library" tab on the code-panel
    def jump():
        turn_left()
        wall_height = 0
        while wall_on_right():
            move()
            wall_height += 1
        turn_right()
        move()
        turn_right()
        for i in range(wall_height):
            move()
        turn_left()

NOTE: remember to use 'import' if using the "Library" tab for functions
      -- i.e. "from library import jump"

In order to solve this final 'Hurdles' puzzle we don't actually need to
modify our WHILE loop from the previous challenge. Instead what we need
to do is make some changes to the 'jump' function (which may be in the
"Library" tab on the code-panel if you moved it before).

By adding a test for the condition "wall_on_right()" and using it with a
WHILE loop we can continue to keep moving up the wall until the right-side
is clear.

Adding a tracking-counter which we update inside the WHILE loop makes
climbing back down the other side of the wall simpler. Since we now know
the height of the wall we can just use a FOR loop to move the counted
number of spaces back down to the ground.
"""
