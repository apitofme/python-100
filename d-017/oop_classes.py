"""
-=< 100 Days of Python >=-
-=[ Day 017 ]=-
"""
# autopep8: off
# pylint: disable=too-few-public-methods,attribute-defined-outside-init,function-redefined
"""
L.117 - How to create your own Class in Python:

In yesterday's lessons and project we learnt to use classes written by someone
else to power our code, in our introduction to object-oriented programming.
Now we will learn how to create our own classes, which is done simply, using
the "class" keyword followed by the name we want to to call the class, and a
colon. Everything that belongs to that class, all of the code for it's methods
etc., is then indented beneath this line.

So, imagine we're building a website, and we want to define a class to model
our website's users...
"""
class User:
    """Models a User object for our website"""
    # everything that's part of the class will go here
    # but we'll leave this empty for now...

# already though, we actually have everything we need
# to go ahead and create an object from our class
user_1 = User()
"""
...and it really is that simple to create a class. Okay so the class we've just
created doesn't do much right now (or anything), but the "class" keyword to
signify that we're defining a class, and then the assignment calling the class
name with parentheses to create an instance of it as an object, is all there
is to it. Everything we write as part of the model within the class can then
be accessed on an object instance using the dot-notation we've seen before.
e.g. "user_1.name" to access the 'name' attribute, or "user_1.logout()" to
call the 'logout' method (once we have written them).
"""

"""
L.118 - Working with Attributes, Class Constructors and the __init__() Function

Now that we have defined our (albeit empty) class, and we have created an
instance of that class as an object, we can actually start to add attributes
to it by simply assigning them as we would any other variable, but prefixing
the variable name we want to use with the class name and the dot notation.
"""
# e.g.
user_1.id = "001"
user_1.username = "jon"
# These are now defined ON that specific object as attributes.
# We can demonstrate this by printing them to the console...
print(user_1.username)
"""
We could then create a second user object and assign different values...
"""
user_2 = User()
user_2.id = "002"
user_2.name = "jen"
print(user_2.name)
"""
...but notice here that we have accidentally used a different name for the
attribute, changing it from "username" on 'user_1' to just "name" on 'user_2'.
Although this is perfectly valid code it could lead to issues later, for
example if we write a function to process user information and the attribute
names aren't consistent across all objects.

Well let's test that. What happens if we try to print an attribute that doesn't
exist on the object...
"""
#print(user_2.username)
"""
We get the following error:
- AttributeError: 'User' object has no attribute 'username'

So, how can we avoid this kind of error without having to just be vigilant
and keep checking ourselves? We can't be expected to remember every attribute
name in every class we create! Also, it's a bit lengthy (not to mention
tedious) if we have to define all of the attributes by hand each time we create
a new object. This is where class "constructor" functions come in.

A constructor is special type of method classses have which, as you might have
guessed from the name, is used whenever a new object is 'constructed' from a
class template. It creates the initial state of an object, by defining it's
attributes at the moment it is created, which is also know in programming as
"initialising" an Object.

Since it is a special type of method, there is a specific syntax we use in
order to define one - it still uses the 'def' keyword but it MUST use the name
"__init__", with double undersocres on each side of the 'init' key name. This
is how the Python interpreter knows that it is this special kind of class
method, which is ONLY used when constructing new instances of the class as
unique objects.

Additionally, the 'init' method requires (at least) one pre-defined parameter,
i.e. "self", which MUST be the first parameter, if others parameters are
defined! This is a special name which represents an internal reference pointer
to the object itself. So whilst referencing an attribute or method in our code
outside of a class is done using something like "Class.attribute" or
"Class.method()", all internal references within the class use "self.attribute"
or "self.method()".

Let's see an example of this now by returning to the car class that we talked
about in yesterday's lessons:
"""
class Car:
    """Defines the code 'blueprint' for creating a car"""
    def __init__(self, seats):
        print("New car being created...")
        self.seats = seats

first_car = Car(5)
print(first_car.seats)

second_car = Car(2)
print(second_car.seats)
"""
Now we can see when we look at and run this code that:

1.  The constructor is called EACH time a new object is created from the class
    - i.e. EVERY time we see "Car()" this is calling the class constructor.

2.  Arguments are passed to the constructor the same way as with any other
    function/method, i.e. between the parentheses (comma separated). The
    values are then mapped on to their respective attributes by the
    constructor. The only difference being that the 'self' parameter does not
    need to be passed in as it is assigned automatically, but it MUST be
    present (and appear first) in the constructor's definition!

Notice however, that now if we try to create an instance of the Car class
without passing in a value for the number of seats, we get an error...
"""
#bad_car = Car()
# -> TypeError: Car.__init__() missing 1 required positional argument: 'seats'
"""
This means that if we define a parameter in a class constructor then, whenever
we call that constructor we are required to provide an argument (i.e. value)
for that parameter, the same as with any function.

Of course there are times when we just want to be able to provide a default
value for an attribute, without always having to pass in a value every time
we crate a new object. For example, thinking about our 'User' class again,
suppose our website was a Blog and we wanted to track how many comments a user
had left. Well when we first create a new user they haven't actually left any
comments yet so it makes no sense to set a value for that when we create the
object. Plus it's extra, unnecessary code to have to assign that initial zero
value each time we create a new User. So, instead we can simple assign any
attribute a default value inside the constructor, like so:
"""
class BlogUser:
    """Model for user accounts on our blog website"""
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.comment_count = 0

blog_user = BlogUser("001", "jeff")
print(f"Username: {blog_user.username}")
print(f"Number of Comments: {blog_user.comment_count}")
"""
The output from this shows us that we have created a new 'BlogUser', assigning
values for both the 'id' and the 'username' to the constructor when we created
the object. The value for 'comment_count' however was assigned from the default
value defined in the constuctor method. You should also start to get an idea of
how the 'self' key name is used to prefix references to class entities from
within the class itself.
"""

"""
L.119 - Adding Methods to a Class

When we create our own classes, as well as adding attributes to store what the
object HAS, we can also add our own methods to provide the functionality for
what the object DOES. We define these methods in exactly the same way as we
do with any other function, i.e. using the 'def' keyword followed by the name
for the method. The only difference compared to a regular function is that a
method MUST have the 'self' reference as the first parameter, just like we did
with the 'init' method. Even if we don't add any other parameter (meaning the
method when called would take no arguments) we must still add 'self' in the
definition. This is just one of the rules of using OOP and classes in Python.

NOTE: Other programming languages that support OOP do not always require an
explicit internal reference to the containing object (though many use "this"
rather than "self"), however part of the concept used in the design of Python
is "Explicit is better than implicit".

To demonstrate how this works let's re-consider our 'User' class from before
and imagine that it is for a social-media website, where a user might have
bot ha count of how many followers they have and how many other people they
are following. We would need a method so that when someone clicks "Follow" on
another user's profile then that user's follower count increases. Of course
this should also increase the "following" count for the user who clicked the
button...
"""
class SocialUser:
    """User model for our Social-Media website"""

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        """Method called when 'THIS' user clicks "Follow" on another user"""
        # increase the "follower" count for the (other) user
        user.followers += 1
        # increase the "following" count for THIS user
        self.following += 1

# Let's create our user objects:
social_user_1 = SocialUser("123", "james")
social_user_2 = SocialUser("456", "jessie")

# Now suppose '1' decides to follow '2', we can call the method:
social_user_1.follow(social_user_2)

# We can print the counts for each to see the result:
print(
    f"Name: {social_user_1.username}; "
    f"Followers: {social_user_1.followers}; "
    f"Following: {social_user_1.following}"
)
print(
    f"Name: {social_user_2.username}; "
    f"Followers: {social_user_2.followers}; "
    f"Following: {social_user_2.following}"
)
"""
As you can see from the output, after calling the "follow" method on the first
'SocialUser' object, and passing the object for the User being followed, we
have successfully increased the respective 'followers' and 'following' counts.
"""
