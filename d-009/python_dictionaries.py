"""
-=< 100 Days of Python >=-
-=[ Day 009 ]=-
"""
"""
L.92 - The Python Dictionary: Deep Dive

>> What is a Dictionary?

A 'Dictionary' in Python is a type of data structure which stores data
using "Key:Value" pairs, where each Key must be unique (within a single
dictionary) and Values can be any arbitrary data object.


So far we have mainly worked with Lists, which are a data structure of a
"Sequence Type" (as are Tuples and Ranges). Dictionaries however are of a
"Mapping Type" as they map 'hashable' values to arbitrary (data) objects.
- Note: The Dictionary is only standard mapping-type built-in to Python!
"""
"""
>> How do we create a dictionary?

We can create a dictionary in several different ways...

The first is using curly-braces '{}', where an empty set of braces will
create an empty dictionary:
    
    - e.g. my_dict = {}

We can also pre-populate our dictionary by defining any number of Key:Value
pairs, with each pair separated by a comma:
    
    - e.g. my_dict = {key1:val1, key2:val2}

We can use a 'comprehension' to generate a dictionary:

    - e.g. my_dict = {x: x ** 2 for x in range(10)}


However there is also the 'dict()' type constructor function...

We can use this to create a dictionary, optionally defining Key:Value
pairs using an equals sign '=' (rather than a colon) to assign Values,
again separating multiple entries using commas:
    
    - e.g. my_dict = dict(key1=val1, key2=val2)

We can use a mapping function to map two separate data structures (of
equal length) together, where the first given provides the Keys and the
second the Values:

    - e.g. my_dict = dict(zip([key1, key2], [val1, val2]))

OR we can pass in an iterable object (such as a List) where each item must
also be iterable and contain precisely two Items, taken as Key and Value
respectively:

    - e.g. my_dict = dict( [(key1, val1), (key2, val2)] )
"""
empty_dictionary = {}

# examples from the Python documentation
# demonstrating dictionary construction methods
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
f = dict({'one': 1, 'three': 3}, two=2)
# the above are all equivalent
# i.e. a == b == c == d == e == f => True

"""
>> So how do we access items in a dictionary?

As mentioned Lists are of the "Sequence Type" which means that they
support Indexing -- i.e. the Index for a given Item is an integer which
represents the Item's position within the sequence. This means that when
we want to retrieve an Item from a List we do so using it's Index number
as a numerical look-up reference.

    - e.g. item_data = my_list[item_index]

Dictionaries however are of the "Mapping Type" and as such are NOT indexed,
meaning Items are stored arbitrarily with no inherent order. A dictionary
has no numerical Index, each Key IS the unique look-up reference for it's
associated Value, hence why each Key must be unique and "hashable". The
syntax we use to address a specific Item within a dictionary however is
the same as we use for Lists, the difference being that we use the Key
instead of an Index reference:

    - e.g. item_data = my_dict[item_key]

Note: An object is hashable if it has a hash value which never changes
during its lifetime.
"""
# given the following dictionary...
programming_dictionary = {
    "Bug": ("An error in a program that prevents the program from running"
            " as expected."),
    "Function": ("A piece of code that you can easily call over and over "
                 "again."),
}

# we retrieve Items from Dictionary by passing the Key as the reference
print(programming_dictionary["Bug"])

"""
>> How can we change a dictionary (i.e. add, update or delete Items)?

Dictionaries (like Lists) are "mutable" -- i.e. their 'value' (contents)
can be changed whilst still retaining the same reference 'name'. Meaning
we can modify the dictionary by arbitrarily adding, updating or deleting
Items as necessary. Even deleting ALL of the Items and then adding more.
The only caveat to consider is that as we mentioned Keys must be unique
and hashable, meaning that Keys should be effectively "immutable". They
can have their associated value altered and they can be deleted from the
dictionary (along with their associated Value) but other than that they
should not change for the lifetime of the Object.
"""
# add another entry to our 'programming dictionary' of terms
programming_dictionary["Loop"] = ("The action of doing something over "
                                  "and over again.")
print(programming_dictionary)

# we can also edit / update a dictionary Item
# by reassigning a new Value to a Key
programming_dictionary["Bug"] = "A moth inside your computer."
print(programming_dictionary)

# reuse our 'empty_dictionary' from earlier and add an item
empty_dictionary["Key"] = "Value"
print(empty_dictionary)
# but now it's NOT "empty" so let's wipe / reset it entirely
empty_dictionary = {}
print(empty_dictionary)  # => {}

# we can also remove individual Items using the 'del' statement
empty_dictionary["Key"] = "Value"
print(empty_dictionary)
del empty_dictionary["Key"]
print(empty_dictionary)

"""
>> Can we loop through a Dictionary like we did with Lists?

Indeed Dictionaries are iterable, however the way we use them with loops
does differ slightly from what we are used to with Lists and it may not
be intuitive to begin with. Let's look at some examples to help clarify:
"""
for thing in programming_dictionary:
    print(thing)
# NOTE: this will actually only print each Key from the Dictionary!
"""
Effectively by default a Dictionary will iterate over it's Keys, then if
needed we can simply use the Key as reference to obtain the Value, e.g.:
    
    for key in programming_dictionary:
        print(key)
        print(programming_dictionary[key])  # => Value

"""
# however this is preferable
for key, value in programming_dictionary.items():
    print(key)
    print(value)
# NOTE:
# - you can get just the keys using '.keys()'
# - you can get just he values using '.values()'
print(programming_dictionary.keys())
print(programming_dictionary.values())

"""
References:
- https://docs.python.org/3.12/library/stdtypes.html#mapping-types-dict
- https://realpython.com/python-sequences/#slicing-in-python-sequences
- https://docs.python.org/3.12/glossary.html#term-hashable
- https://docs.python.org/3.12/glossary.html#term-mutable
"""

"""
L.93 - Coding Exercise: Student Grading Program
"""
# See external file: "exercise_student_grades.py"
