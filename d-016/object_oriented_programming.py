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
