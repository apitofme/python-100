"""
-=< 100 Days of Python >=-
-=[ Day 010 ]=-
"""
"""
L.100 - Functions with Outputs

>> Quick Recap on Functions:

Functions allow us to create a block of code associated with a given name
which when we call the name executes that particular block of code. This
helps us to create contextually focussed, reusable pieces of code so that
we can perform the same operation multiple times without the need to type
out the same code again and again.

Note however that these are not necessarily operations which we want to
perform consecutively, as for that we might use a loop. Rather, they allow
us to break down tasks in to simpler, repeatable steps. helping us to keep
each piece of code focussed on a specific task as well as keep the code
cleaner and tidier and therefore easier to read and understand.

We started off using a 'basic' function with no input parameters.
Which to remind us we create using the 'def' keyword followed by a name
(which should be clear and descriptive, with underscore-separated words)
then a set of parentheses.

    def my_basic_function():
        # code to execute
        # when function is called
        # goes here

Then we introduced input variables (arguments) which allow us to pass data
(parameters) in to the function. The data being assigned to 'local'
variable names within the context (scope) of the function, for processing.

    def my_function_with_inputs(arg1=param1, arg2=param2):
        # code to execute when function is called
        # using the parameter-values stored in the arguments


>> Functions with Outputs:

Quite simply, a function with an output is one that OUTPUTS some data and
RETURNS it to the piece of code that called the function. To do this we use
the 'return' keyword followed by the variable name of the data object to be
returned.

    def my_return_function():
        # function processes some data
        # ultimately giving us the result of that processing
        # i.e. result = result_of_processing
        # then we return that result...
        return output

The data/value contained in the result is returned to the place in the code
where the function was called, so we might typically use a variable
assignment to capture and store the returned data.

    result_of_function = my_return_function()


Let's have a go with some examples to see how this works.


>> Challenge exercise:

Create a function called "format_name" which takes two arguments, one
called "f_name" (first name) and one called "l_name" (last name).
We want this function to return the name in "TitleCase", where each word's
first letter is capitalised.
"""


def format_name(f_name, l_name):
    """exercise showing a function with a return"""
    return f"{f_name.title()} {l_name.title()}"


print(format_name("doUgLaS", "ADaMs"))  # => "Douglas Adams"

"""
L.101 - Multiple Returns:

A single function may have have multiple RETURN statements. However it is
important to understand that once a function reaches a 'return' statement
no other code in that function will be run, much like the 'break' keyword
in a loop. Since the 'return' keyword terminates the function at the point
it occurs then only one 'return' will ever be executed. Multiple return
statements must therefore be implemented using additional logic (such as
conditional statements) to branch the function's code in to separate
distinct return paths.
"""


def format_name_v2(f_name, l_name):
    """exercise showing a function with multiple returns"""
    if f_name == "":
        return "You did not provide your first name"
    if l_name == "":
        return "You did not provide your last name"
    return f"{f_name.title()} {l_name.title()}"


print(
    format_name_v2(
        input("What is your first name? "),
        input("What is your last name? ")
    )
)

"""
L.10_ - Coding Exercise: 
"""
# See external file: "exercise_.py"
