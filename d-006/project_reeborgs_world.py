"""
-=< 100 Days of Python >=-
-=[ Day 006 ]=-

Project: Reeborg's World

The project for today is a little different as we'll be using an external
website called "Reeborg's World" which (to quote the site) "is intended to
help beginners to learn programming, using Python".

NOTE:
    It is effectively a web based version of the author's previous Desktop
    Application "RUR-PLE" -- Ref: https://en.wikipedia.org/wiki/RUR-PLE
    The concept is similar to that of TURTLE (for those old enough to
    remember that!) -- Ref: https://en.wikipedia.org/wiki/Turtle_graphics

Topics we'll cover along the way include:
- Code Blocks and Indentation; Functions; WHILE Loops and more...


>> Reeborg's World: Escaping the Maze
-- https://reeborg.ca/reeborg.html?lang=en&mode=python&url=worlds%2Ftutorial_en%2Fmaze1.json

World Info:
Reeborg was exploring a dark maze when the battery in it's flash-light died.

Write a program using an if/elif/else statement so Reeborg can find the exit.
The secret is to have Reeborg follow along the right edge of the maze,
turning right if it can, going straight ahead if it can't turn right,
or turning left as a last resort.

What you need to know:
    - The functions move() and turn_left().
    - Either the test front_is_clear() or wall_in_front(), right_is_clear()
      or wall_on_right(), and at_goal().
    - How to use a while loop and if/elif/else statements.
    - It might be useful to know how to use the negation of a test
      (i.e. "not" in Python).
"""
"""
>> Solution:

    def turn_right():
        for i in range(0,3):
            turn_left()

    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

"""
"""
Now there are actually edge cases where the solution above doesn't work,
meaning there are certain start locations in certain maze configurations
that result in the code above getting stuck in an infinite loop, never
reaching the goal.

Thankfully the Reeborg's World website allow you to save and load specific
Worlds, so rather than having to reload the page repeatedly until one of
these edge cases turns up you can load World from a file. There are three
files included in the course resources for today that you can use to test
and hopefully "debug" the code in the solution above, to improve it so that
it passes all of these edge case scenarios as well.


>> Solution v2.0:

    # if using "turn_right" from the Library tab, import it!
    from library import turn_right

    # until we reach our goal...
    while not at_goal():

        # we want a wall on our right
        if wall_on_right():
            # keep the wall on our right for as long as possible
            while wall_on_right():
                if front_is_clear():
                    move()
                else:
                    turn_left()
            continue
        
        # when forward progress is blocked...
        elif wall_in_front():
            # turn Right if possible
            if right_is_clear():
                turn_right()
                move()
            # otherwise turn Left
            else:
                turn_left()
            continue
        
        # when there is no wall in Front or to the Right...
        else:
            turn_right()

            # then, until we find another wall on the Right...
            while not wall_on_right():
                # move Forward if we can
                if front_is_clear():
                    move()
                # if not then turn Right if possible
                elif right_is_clear():
                    turn_right()
                # otherwise turn Left
                else:
                    turn_left()

Not going to lie this was a LOT trickier than I expected to pass all three
test files AND still pass the regular random Maze! Needless to say I cannot
guarantee this solution has a 100% success rate, but it passes all 3 test
scenarios and my limited random testing.

During my struggle I was getting tempted to simply use a rotation tracking
variable in order to test if 360 degrees of rotation had occurred due to a
circular path (which would mean an infinite loop), but that felt like a bit
of a hack so I held out hope for a LOGICAL solution.

In the end my solution was based on the idea of finding a wall and getting
it on to the right-hand side, then sticking to it for as long as possible
(as per the 'World Info' brief). This meant turning right as soon as there
was no wall to the right, BUT then using a loop to keep moving until there
was a wall to the right once more. This loop involved moving Forward if
possible, only turning Right when Forward was not possible, and then only
turning Left when no other possibilities remained. -- This is really only
what the 'brief' for the Maze Challenge explained, but implementing it in
a way that functioned as expected proved to be quite difficult!


>> Angela's Solution:

This proved to be a much simpler and more succinct solution than mine above.
Honestly I did initially have the thought that (in order to FIX this 'bug'
with the Maze Challenge) the FIRST thing to do is move until I hit a wall,
then turn Left to put that wall on the right-hand side of me.

Unfortunately my brain wasn't braining so good so I didn't think to put this
OUTSIDE of the main loop in order to escape any difficult starting positions
(So I'd persisted to attempt to find a solution that worked INSIDE the loop!)


    # THIS is how we 'fix' our edge-case problems causing infinite loops
    # FIRST we move Forward until that is no longer possible
    while front_is_clear():
        move()
    # NOW there is a wall in Front of us so we simply need to 
    # TURN LEFT in order to put the wall on our right-hand side
    turn_left()

    # So this part is the same as the original 'buggy' solution
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()

"""
