"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-
"""
"""
L.46 - IndexErrors and Nested Lists

>> List Indexing Errors:

One of the most common errors you might see when using Lists in Python is:

    "IndexError: list index out of range"

This occurs when you try to use an index (offset) for an Item in a List
that doesn't exist -- i.e. you try "list[5]" when there are only 4 Items
in the List.

This get's doubly confusing when we know how many Items are in a List,
perhaps from using the 'len()' function, but we forget to account for
the fact that the First item is at index 'offset' zero ("list[0]").

As we've described before, Lists always start counting from 0 because
what we're actually counting isn't the item's numerical position but
it's offset from the First item (i.e. the start of the List). The first
item has no offset because it IS the First item, so it's offset is "0".

This means that in our example where we tried to use the index "5" on
a List containing only 4 items, the highest index we could give before
we get an error is actually "3"...

    List Index  | 0 | 1 | 2 | 3 
    ----------------------------
    List Item   | 1 | 2 | 3 | 4

This zero offset indexing means that the number of addressable elements
in a List is always "len(list) - 1" and is the reason why typically
programmers will get an 'IndexError' when they're off-by-one!


>> Nested Lists:

Each year, the Environmental Working Group releases its "Dirty Dozen",
a list of the 12 fruits and vegetables consumers typically buy that are
laden with the most pesticides -- ASIDE: All produce are actually washed
and peeled BEFORE they are tested!

So let's work with this list as an example...
(because it's shorter and therefore easier than the list of US States!)
"""
# Here's the list of the top 12 pesticide offenders of popular produce
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
               "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes",
               "Celery", "Potatoes"]
# Note that there is a mix of Fruits and Vegetables in the list.
# What if we wanted to separate the Fruits from the Vegetables?
# - We could simply create two separate Lists:
fruits = ["Strawberries", "Nectarines", "Apples",
          "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
# BUT this separates items that are contextually related
# (i.e. they're all on the "Dirty Dozen" list)
# - Then we can put these two separate lists INSIDE a "Dirty Dozen" list:
dirty_dozen = [fruits, vegetables]
# We now have a list containing two other lists
# The lists are "nested" inside the outer list [Remember 'nested' IFs?]

# Let's take a look at what this looks like when we print it out:
print(dirty_dozen)

"""
L.47 - Coding Exercise: Treasure Map
"""
# See external file: "exercise_treasure_map.py"
