"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-
"""
"""
L.44 - Understanding the Offset, and Appending Items to Lists

>> Data Structures: - Lists

In Python there are many different types of 'data-structures' we can use
to give logical or organised structure the data we store in our variables.

Until now we have only used a variable to store a single piece of data at
a time by assigning it (e.g. "variable_name = data_value"), but what if we
want to store grouped pieces of data, data that logically goes together?

For example, it doesn't make sense to store the names of each state in the
USA in separate variables when contextually they belong together. In this
case it would be much more convenient to have a variable named "us_states"
that contained ALL of the state names.

Equally there may be times when we want to have an order to some data, be
it numerical, alphabetical or simply the order in which they were added.
Such as if we wanted to keep track of a customer queue, where the person
who joined last should not get to go first, or really before anyone who
joined the queue before them!

One of the most useful and common data-structures available to you in
Python is the 'List', which is represented in code as a pair of square
brackets with many items stored inside -- e.g. [ item1, item2, ... ]
where each item is separated by a comma ','

Lists set no restrictions on the specific data-type of each item, they
can be strings; integers; floats etc. or any combination thereof.
"""
# A simple example could be a list of your favourite fruits
my_fav_fruits = ["Apple", "Watermelon", "Banana", "Cherry"]
# We can also see how this is represented when we print it out
print(my_fav_fruits)

# Taking the example of US States, previously we might have done this:
state1 = "Delaware"
state2 = "Pennsylvania"
# ... etc.
# BUT now we know about Lists we can store all of these in one cohesive
# data structure, e.g:
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia"]

"""
In much the same way as we did previously with Strings, we can access
individual Items within a List using their index position ... which if
you also remember, starts at zero!
    -- e.g. states_of_america[0] => "Delaware"
            states_of_america[2] => "New Jersey"

It is easier to understand this if you think of the number as an "offset"
from the start, rather than the 'position'. So with an offset of 0 (zero)
we get the first Item, then if we offset by '1' we get the second Item
and so on.

Equally with Lists, as with Strings previously, we can use a negative
offset to count backwards from the last Item in the list:
    -- e.g. states_of_america[-1] => "Georgia"
            states_of_america[-3] => "Pennsylvania"

In fact let's confirm that by printing the output:
"""
# positive index offset
print(states_of_america[0])
print(states_of_america[2])
# negative index offset
print(states_of_america[-1])
print(states_of_america[-3])

"""
Items in a List are considered "mutable", meaning they can be changed.
Just as we can reassign the value stored on a variable we can change the
data associated with an Item in a List.

Suppose we decided that "Pennsylvania" was spelt wrong, then we could
update the List by reassigning a new value to the Item using the same
square-bracket referencing method:
"""
states_of_america[1] = "Pencilvania"  # LOL
print(states_of_america)

# It doesn't even have to be the same data-type
states_of_america[1] = 222
print(states_of_america)

"""
Remember how Strings have methods (functions) we can call on them to
perform different actions, such as 'lower()' to lower-case the String,
well Lists have methods too. So if we want to add a new item to the list
we can call a method on the list object to do so, in this case to add an
item to the end of the list we use 'List.append(new_item)':
"""
states_of_america.append("Connecticut")
# When we print the list now the new item will be the last item
print(states_of_america)

"""
Of course there are a whole lot more besides 'append()', and we can see
some more information on the available List methods in the official Python
documentation:
- https://docs.python.org/3.12/tutorial/datastructures.html#more-on-lists

For example to add multiple new items we can actually just 'extend()' the
current list with another List, which we can simply create using square
brackets directly inside the parentheses, passing the new list in as the
function-parameter:
"""
states_of_america.extend(["Massachusetts", "South Carolina"])

# OR we could have created the new list as a named variable first
more_states = ["Virginia", "New York", "North Carolina"]
# Then passed that in as the parameter
states_of_america.extend(more_states)
# BUT the first way, passing the new list in directly, is better since
# we're not creating an extra variable unnecessarily and taking up memory

"""
L.45 - Coding Exercise: Banker Roulette
"""
# See external file: "exercise_banker_roulette.py"
