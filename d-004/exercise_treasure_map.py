"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-

Coding Exercise: Treasure Map (L.47)
"""
"""
Slide 1: Task
- Write a program that will mark a spot on a treasure map with an "X".

In the setup for this exercise we'll create 3 list variables, each one
containing 3 items (or "elements"). We will then create another variable
which will hold all of these as nested lists -- Conceptually this will
provide us with a 3 x 3 grid for our Treasure Map.

If we print the 'map' (variable) out with a line-break between each 'row'
(nested list), in order to visually stack the lists on top of each other,
then imagine an overlaid co-ordinate system we should get the following:

           A     B      C
        
    1   ['⬜️', '⬜️', '⬜️']

    2   ['⬜️', '⬜️', '⬜️']

    3   ['⬜️', '⬜️', '⬜️']


Given 2-character input corresponding to a grid co-ordinate, in the
format of a Letter followed by a Number (e.g. "A1"), your program must
convert this input to a usable format then determine where (and how) to
store an "X" in the 'map' variable so that it is displayed in the correct
location when printed out.
"""
# Let's setup the exercise
row_1 = [" ", " ", " "]
row_2 = [" ", " ", " "]
row_3 = [" ", " ", " "]
treasure_map = [row_1, row_2, row_3]
print("Hiding your treasure! X marks the spot.")
position = input()  # Where do you want to put the treasure? -- e.g. "B3"

"""
Slide 2: Solution
"""
# Create a list of the column references [1]
columns = ['A', 'B', 'C']
# The 'row' reference is the 2nd character of the input, minus one
row = int(position[1]) - 1
# The 'col' reference is the index of the column Letter in 'columns' [2]
col = columns.index(position[0])
# Then we use these references to update the value stored in the 'map'
treasure_map[row][col] = 'X'
"""
[1] This effectively maps the column Letter to it's index value
    -- i.e. "A" is at index '0', "B" is at '1', "C" is at '2'
[2] We can use the 'index()' method to look up the Index for a given value
    Ref: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
"""
"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/e806e25c-5f84-4d7c-9c7c-2c0fcd0bfe84?sl=5a6962c9-0e42-448b-b7df-0616c6d30431&st=SEfB5kQTLxCzgxd1DdyJRDPpY9Rp1HhB
"""
