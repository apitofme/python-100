"""
-=< 100 Days of Python >=-
-=[ Day 016 ]=-
"""
"""
L.108 - Why do we need OOP, and how does it work?

If we look back over our Python programming journey thus far, we should see
that there have been a couple of fundamental concepts introduced to us that,
above all others, stand out as ones that have elevated both our code and our
capabilities as programmers. Namely "loops" and "functions", which have made
performing repetitive tasks easier and have also enabled our code to act more
powerfully. In doing so, these features have made greater and more complex
programming functionality available to us.

We can think of each time we have learnt one of these features and started to
master it as "levelling up" our programming skills. Now, Object-Oriented
Programming (or 'OOP' for short) is the next one of these pivotal concepts we
will learn that will again allow us to level up and exponentially increase
the capabilities of our programming skills to tackle larger and more complex
challenges.

Up to now we have been learning to write our programs in what is referred to
as a "Procedural" (or 'Functional') programming style -- i.e. using functions
(a.k.a. procedures) to compartmentalise our code efficiently. As such, our
programs, in general, have operated in a mostly linear fashion, running from
the top to the bottom of our code from a single file. As our programs have
grown in size and complexity, you might already have started to notice how
quickly they can become difficult to keep track of. Here you can think of OOP
as doubling down on the advantages that using functions gave us, taking
compartmentalisation and the deliberate structuring of code for reuse to the
next level.

Whilst moving to an OOP approach does introduce additional complexities, it's
main advantages generally outweigh the logistical overheads of implementing a
program using this paradigm (for a program of sufficient size and complexity).
The immediately notable difference from what you have been used to is OOP's
implicit tendency towards using multiple files, since in OOP we implement
logical groupings of functionality into conceptual 'objects' called "Classes".
Although not an explicit requirement, these often reside in their own files,
or at least in files grouping together classes that provide related and/or
interoperable functionality.

This 'horizontal scaling' approach to code organisation and management can be
seen as another advantage of OOP when dealing with larger projects. Especially
when working collaboratively with other programmers, as it allows a project to
be broken down into smaller modules, where individual developers may focus on
providing specific components of functionality -- e.g. user interfaces,
database interactions, user input forms, etc.

In fact, it is fair to say that some of the advantages of OOP are almost, if
not, of greater benefit to the organisational logistics and delegation of
project management than they are to the individual programmer.


>> Time for an example:

Imagine we were tasked with creating the program for a self-driving car.
Granted this is several levels of complexity greater than the Coffee Machine
project, but let's approach it the same way. We've learnt to tackle these
problems initially by breaking them down in to smaller parts, so...

Q. What is a self-driving car? What are the different components it requires?

    1. A camera module, to watch the road ahead
    2. Lane detection, to keep the car on the right part of the road
    3. A navigation module to track and plot routes to destinations
    4. Some form of fuel management system

Of course that's just a very simplified example, there is a lot more that a
self-driving car would need in order to function safely. What's important
though is that already we've identified several key modules which would need
to be developed.

Now imagine that we have a whole bunch of people working for us to develop
this car. Splitting these tasks up between everybody, by assigning groups of
people as dedicated teams to work on each module, means that they can all be
working to produce these different components simultaneously. This greatly
increases productivity and will reduce the time it takes for us to build all
of the software we need for this car.

Once they're built, all of these individual modules would be reusable. Imagine
that after we'd finished developing the software for the car we got a new
project to develop software for a drone parcel delivery system. A lot of those
components could be useful since the drone would also need a camera,
navigation, fuel/battery management etc., and because we used OOP to build
these features as modules (i.e. compartmentalised blocks of functionality) we
can take them out of the car project and reuse them, so we won't have to code
them up again as we might need to if we'd been using procedural programming.


>> So what exactly is Object-Oriented Programming:

As we've already covered, OOP allows us to split a larger task in to smaller
pieces, each of which can then be worked on by separate people or teams of
people, and each piece becomes a reusable module, so if we need the same
functionality again in the future we don't have to write it all over again
from scratch.

OOP actually allows us to do much more than this though...

Imagine you've inherited a restaurant from a long lost uncle, and you realise
that it's actually really hard running a restaurant...

1. You have to be the receptionist, taking bookings etc.
2. You have to be the waitress, taking orders and serving to the tables
3. You have to be the chef and cook up the orders as they come in
4. You also have to be the cleaner, tidying up after everybody has left

So what if you just hired some staff to do each specific job, they're
experienced so they already know how to do their job. Then you can just act as
the manager and tell the staff what to do, you don't need to know the details
of how they do their jobs. It is these concepts that we can use to simplify
the relationships in our code and make it scalable for larger and more complex
projects.
"""

"""
L.109 - How to use OOP: Classes and Objects

Picking up from the previous lesson's example where you've inherited a
restaurant and hired a bunch of staff to fill the different roles you need
(chef, waitress, cleaner etc.), leaving you to be the manager ... you might be
thinking "how does this relate to OOP", so let me explain.

The "object" in Object-Oriented Programming refers to the fact that we are,
generally, attempting to model a real-world object in to code. Taking it
conceptually as a set of properties and functions, behaviours or actions.

So let's start by turning our hypothetical restaurant in a virtual one, we
will need to model a digital version of each or our types of staff. Taking our
waiter as an example we could begin to model it by saying that, conceptually,
there are probably two things we need to think about: what it HAS, and what it
DOES.

In terms of what it HAS, well it might have variables like:

    is_holding_plate = True
    tables_covered = [2, 5, 6]

Now it also has things that it DOES:

    def take_order(table, order):
        # takes order to chef

    def take_payment(amount):
        # add money to restaurant

We can see from our model that, what the waiter HAS and what the waiter DOES,
are the two most important things that make up our 'waiter' object. These are
referred to as the object's "attributes" and it's "methods". Where 'attribute'
is basically a fancy word for a variable associated with a modelled object,
and a 'method' similarly is a function associated with a modelled object. They
aren't regular variables and functions that we've used in our code up to now,
they are part of the 'waiter' object, so in order to use them we must have
access to a waiter.

There are a lot of words and specific language associated with programming,
and OOP is no different. It may take some time to learn to understand what
each special word means, but in time they will all become a part of your
internal programming dictionary. The important thing to know for now is that
an object can have attributes, typically modelled with variables, and they can
also have methods, modelled with functions. So an object is just a way of
associating some pieces of data (attributes) with some functionality (methods).

The code structure we use to define the model for an object is called a
"Class". The important thing with this model is that it isn't the object
itself. What we have done above is define WHAT a waiter IS, and what it does,
but this applies to any waiter. Often a restaurant will have several waiters,
each responsible for different groups of tables for example. So the class is
really only the definition of the object, a template if you will. Once we
have written the class we can create as many waiters as we want using this
template. We create an object from a class, as many as we need, each one is an
object but each is also unique. So one waiter can be responsible for tables
4, 5 and 6, whilst another can be assigned to 1, 2 and 3. One might be
carrying a plate, another not. One might be taking an order, whilst another is
taking a payment. Each waiter is a unique instance of the waiter class/object.
"""

"""
L.110 - Constructing Objects and Accessing their Attributes and Methods

You can think of a 'class' as a blueprint, it is the design document from
which the actual object(s) are built. In order to get an object in our code
we need to create an instance of the class using, the syntax we use to do this
looks like the following example:

    car = CarBlueprint()

Class names are distinguished from other names as they are written with the
words concatenated together (i.e. no underscores) and the first letter of each
word capitalised, this is often referred to as "Pascal Case". As you can see
the class name is on the right-hand side of the assignment operator, i.e. it
is the thing being assigned. The object reference then, is the name the class
is being assigned to, on the left-hand side of the operator.

Once we have an object (an instance of a class) we want to be able to access
the attributes and methods of that object, i.e. the variables and functions
provided by, and associated with, the object. To do this we use the 'dot'
syntax, which you have probably seen before when we've imported modules to
use in our code. The syntax is simple, here's an example:

    car.speed

First we put the name of the Object we want to use (e.g. 'car'), followed by
a 'dot' ("."), and finally the name of the attribute we want to access, in
this case "speed". This would give us the value stored in that attribute, on
that specific car object. Remember each object is a unique instance of the
class used to create it, so if we had created more than one car object they
could all have different values stored in that named attribute, and we would
only get the value from the specific instance we're referencing.

We can reference methods (functions of the object) in much the same way, the
notable difference being that we need to use a set of parentheses after the
named reference to actually call the method, e.g.:

    car.stop()

Other than the dot-notation used to reference them they behave in exactly the
same way as other functions, they're only called "methods" because they're
associated with an object. They are defined using the "def" statement, they
can take arguments, and they can return values, just like any other function
we have made and used up to now. Arguments are passed between the parentheses
as normal, for example:

    car.accelerate(50)

...could be used to accelerate the car to 50 mph/kmh.
"""

"""
L.111 - How to Add Python Packages and Use PyPI

Thankfully we don't have to write all of our own classes, and we've talked
before about taking advantage of code already written by other developers. In
fact Python has probably one of the largest ecosystems of freely available
packages for people to install and use in their own code. The most common
platform to discover these and install them from is called PyPI (short for
the "Python Package Index") which can be found here: https://pypi.org

We have used and created 'modules' for ourselves in our own projects before,
as single files containing resources we wanted to import in to our main code
file (e.g. ascii-art, lists of data, etc.). Packages differ from modules
because they are much larger and contain multiple files or sub-modules, where
the code has been packaged together with a specific goal or purpose in mind.
Such as providing the means and functionality to interact with a particular
file type, or to create and manipulate certain types of data.

In addition, whilst previously we have only used modules we have created for
ourselves, or we have imported packages that are included (by default) with
every standard Python distribution, and so have always been available to us.
Any other package we might want to use however, we must first install from
PyPI (or wherever) in to our local Python library, to make the package
available to use with the "import" statement.

Let's suppose that we wanted to be able to create a table of different
Pokemon characters in a way that allowed us to document their different types
(e.g. Pikachu is an Electric type etc). We might then want to be able to
print that table out to the console in a way that looked...well, like a table.
- e.g.
        =============================
        | Pokemon Name |    Type    |
        =============================
        |   Pikachu    |  Electric  |
        -----------------------------
        |     etc.     |    etc.    |

Doing this ourselves, manually, by figuring out the spacing, then formatting
the necessary output strings to `print()`, so that it all lined up and looked
pretty, would be a laborious and daunting task. Thankfully other people
have already solved this problem before, and since they were kind enough to
publish their efforts as a Package, we can leverage their work to make ours
easier. We just need to pick a package that provides the features we want,
download and install it locally so we can use it.

For the case of our Pokemon table, if went ahead and searched on PyPI for
something like "ascii tables" we would see a whole bunch of projects come up,
some of which sound like they would do what we want, but others less so. To
save time let's just agree to choose a package called "PrettyTable"...
- https://pypi.org/project/prettytable/

There many possible ways you could install this package, depending on your OS,
code editor (IDE), how you installed Python, and whether or not you are using
a virtual environment (venv). For simplicity's sake, the default and most
consistent way however is from the command line using something called "pip".
This should be included with any standard Python distribution and will install
the package to your global python environment.

You can find a guide here:
- https://packaging.python.org/en/latest/tutorials/installing-packages/

...more specifically, once you are sure that 'pip' is available to run:
- https://packaging.python.org/en/latest/tutorials/installing-packages/#use-pip-for-installing

But essentially PyPI is set up so that you can simply copy the command from
the page of the package you want to install, paste it in to your terminal
console and run it, e.g.:

    pip install prettytable

If this command doesn't work you may need to refer to the guide linked above.

We can then test to make sure we can use it in our project with the following
line of code:
"""
from prettytable import PrettyTable  # nopep8
"""
Run the file and if there are no errors then you have successfully installed
the PrettyTable package from PyPI, congratulations. We'll pick up the next
steps and actually start using this package to format our output in the next
lesson.
"""

"""
L.112 - Practice Modifying Object Attributes and Calling Methods

Now that we have the 'prettytable' package installed we can look at how we're
going to use it.

NOTE: There's some documentation right on the package's page on PyPI:
- https://pypi.org/project/prettytable/

First we need to import the package, but rather than just "import prettytable"
we can specify the class we want to use and just import that specific module,
i.e. "from prettytable import PrettyTable". Notice the 'Pascal Case' of the
name on the right-hand side, after the keyword 'import', this denotes that
it's a Class.

We already have our import statement above though, so we can use that rather
than re-import the package (which would cause a warning with PyLint). So the
next thing we need to do is create our object from the class we've imported.
"""
table = PrettyTable()
"""
This creates an instance of the PrettyTable class and saves the new object
to the variable name 'table'. Already, if we go ahead and print the variable
we will see the barebones of a table (with no data)...
NOTE: Printing the type() will show us that the object is an instance of a
'class', specifically the PrettyTable class within the prettytable module.
"""
print(f"Type: {type(table)}\n")
print(table)
"""
Now, using the documentation, let's add some columns and data to our table
so that we can display some information about our Pokemon in a nice formatted
output...
"""
table.add_column(
    "Pokemon",
    ['Pikachu', 'Squirtle', 'Charmander']
)
table.add_column(
    "Type",
    ['Electric', 'Water', 'Fire']
)

# we can print the table again to see the information above displayed 'pretty'
print(table)
"""
Okay so there we have the formatted output, and we have called a method on an
object to do so. Remember that we can also change the attributes of objects,
so let's have a look at how we can do that using our PrettyTable.

For example if we wanted to change the appearance of our table then we can
simply change the values of some of the attributes that govern the table's
visual style. For example if we wanted to change the alignment of the text
in the table's columns we could use the "align" attribute...
"""
table.align = "l"
print(table)
"""
Notice here we assign a value, as opposed to passing an argument in
parentheses, because this time we're referencing an attribute (i.e. variable)
rather than calling a method (i.e. function).

You can see a list of some of the attributes you can change by reading through
the documentation. An older but perhaps simpler version of which can be found
here: https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

So we have covered how to create an object, how to access and call methods on
the object, and how to access and update values of the object's attributes.
Although this is a relatively simple demonstration, the way you create and
interact with objects is the same regardless of how complex the program or
class definition.
"""

"""
L.112 - Python Objects Quiz
"""
# Completed on Udemy

"""
L.113 - Building the Coffee Machine in OOP

One of the great things about OOP, when taking advantage of pre-written
modules and packages, is that we don't have to know or understand how the
implementation of a given piece of code works, we just need to know and
understand how to use it (e.g. by importing and calling methods etc.). We
can just trust that it does what it says it does, then we can install it and
import it and use it in our code as a part of our program.

As a demonstration of how to do this we are going to re-implement the "Coffee
Machine" project from before, but this time using OOP. The resources will be
provided so we don't have to write our own classes, we can just import them as
modules, as though we'd installed an external package. Then we can create and
use the objects made available to us by these classes, and solve the problem.
This will have the same criteria as before, so it will need to have the same
functionality, accept the same inputs etc. -- Documentation is provided, to
explain each of the classes and what different attributes and methods are
available on each.

Once you have downloaded and extracted all of the necessary course resources
in order to tackle this project, you can go ahead and start adding your code
to the "main.py" file for your solution.
NOTE: You should NOT edit or alter any of the other files in any way! Treat
them as though they are an external package you have installed in order to
help you build out this project.
"""
"""
NOTE:
The project can be located in the "project" sub-folder for today, whilst the
resources (including start-file archive) are located in a separate sub-folder
INSIDE the project folder.
"""
