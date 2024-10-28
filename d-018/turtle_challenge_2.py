"""
-=< 100 Days of Python >=-
-=[ Day 018 ]=-
"""
from turtle import Turtle, Screen
"""
L.130 - Installing Packages, Importing Modules and Working with Aliases

At this point I feel it is worth going over the import statement in a bit more
detail, as we have seen a couple of different ways of using it, so let me
explain their differences now:

    1. Basic Import:

        e.g -- "import turtle"

    Here we just have the keyword 'import' followed by the module name (in this
    case 'turtle'), essentially this statement imports the *entire* module as a
    single entity. This means that in order to use a component from the module
    (i.e. a Class) we would have to reference it using dot-notation, prefixing
    the name of the class with the module name, e.g.:
    
        my_turtle = turtle.Turtle()

    -- Where "turtle" (lowercase 't') is the module name, and "Turtle"
    (uppercase 'T') is the Class name inside that module.


    2. Specific Import:

        e.g. -- "from turtle import Turtle"

    This syntax however allows us to specify individual components (Classes)
    from a given module, using the 'from' keyword to identify the module,
    followed by the 'import' keyword to identify the specific Class. The
    advantage with this is that it allows us to reference the class name
    directly, without having to use the dot-notation module name prefix, e.g.:

        my_turtle = Turtle()

    -- Useful when you want to use a class name often, so you have a shorter
    means of referencing it.
    
    You can import multiple classes from the same module this way by separating
    each name after the 'import' keyword with a comma. Although this is
    typically limited to 2 or 3 names, and some coding standards prefer a
    seaparate lien for each import.

    NOTE: It is also possible to import *every* class from a module by using
    and asterisk '*' in the place of a specific Class name. However this is
    NOT considered good practice, as it can lead to confusion over where a
    specific Class or function is defined. You should avoid this, but in case
    you coma across it "in the wild" it's worth knowing what it means and what
    it does!


    3. Aliasing Modules:

        e.g. -- "import turtle as t"

    This syntax allows us to assign an alias name to the module when we import
    it, allowing us to reference it using *that* name instead, e.g.:

        my_turtle = t.Turtle()
    
    -- This is useful when a module has a particularly long name and you want
    to create a shorter reference to use locally in your code.


>> Installing Modules:

An import statement only works when a module is available to the local version
of Python we're running. So, whilst "turtle" is included with the Python SDL,
there are a huge amount of 3rd-Party modules available which do not come
installed as standard (such as "request", "prettytables", "numpy" or "pandas"
for example). In order to use any of these modules we have to install them
from a package first (e.g. from PyPI using "pip").

If we try to import a module that is not available locally we will get an error
when we run our code (e.g. "No module named _"). If you get such an error it
is an easy way to know that the module you are trying to use needs to be
installed.

NOTE: A package is installed to a specific local instance/version of Python
(i.e. you're project's "virtual environment"), and will ONLY be available to
this instance. This means that if you try to run code that depends on a
3rd-Party module, on a different instance of Python (such as on another
computer), it will fail unless the required modules are also installed there.


>> What is a "virtual environment"?

Python projects are typically developed in what we call "virtual environments",
which are effectively containers for a local Python installation specific to
each project. They contain a Python interpreter (usually the full SDL), as well
as any additional modules required by the project. Thereby providing a
dedicated environment where all of the requirements necessary to run the
project are met. This ensures the portability and operability of the project
across different machines, enabling the project to be shared without issue.

Virtual environments are necessary because, as the Python language evolved, a
new major version (3.x) was released that was not 100% "backwards compatabile"
with the previous version. This resulted in a dichotomy between the older 2.x
series and the newer (current) 3.x version. Since a notable portion of the
Python module eco-system was still shouldered by code written for 2.x it caused
significant issues for the Python community. Such that migration from 2.x to
3.x has taken a protracted amount of time and could still be considered
"on-going"!

Additionally, since individual 3rd-Party modules are written and maintained
separate from one another, they may also have their own incompatible changes
and specific versional requirements for both the Python interpreter and/or
other packages they rely on. Therefore, due to this potential for errors and
version conflicts, the simplest solution for the Python community was to adopt
the use of self-contained development environments. Ensuring that all of the
required components, at any specific version necessary, are packaged together
and able to be distributed with the code, allowing the project to be run
consistently and without issue, anywhere.

The one notable caveat to this system of compartmentalisation however is that
packages MUST be installed on a 'per environment' basis. So, if you want to use
the same module in several projects it must be installed for each one.
Thankfully this can be handled efficiently by virtual environment managers,
such that any specific package/version file is only downloaded and stored to
disk once, in a central repository. Individual project environments requiring
a specific package are then linked back to the that centralised instance by
reference (e.g. a filesystem "symbolic link").


NOTE: It is possible to install packages "globally" (i.e. in the system level
version of Python installed), but these will still only be available to code
being run on *that* specific Python installation. Hence is not recommended.
"""

"""
L.131 - Turtle Challenge 2: Draw a Dashed Line
"""
brush = Turtle()

for _ in range(25):
    # Always move forward 10 paces...
    brush.forward(10)
    # ...but alternate whether the pen is down (draws) or up (does no draw)
    if brush.isdown():
        brush.penup()
    else:
        brush.pendown()

# Keep the display window open until we click on it
window = Screen()
window.exitonclick()
