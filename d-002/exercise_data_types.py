"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-

Coding Exercise: Data Types (L.21)
"""
"""
Slide 1: Task - Add the digits in a 2 digit number
- e.g. if the input is 35 then the output should be 3 + 5 which equals 8
"""
two_digit_number = input()

"""
Slide 2: Solution

- First, if we type check our input using the 'type()' function we see that
we are working with a string. (Note: This is not essential to the output of
the program but it helps us to think about the problem, and use what we've
already learned, to come up with a solution.
"""
print(type(two_digit_number))  # => 'str'
"""
- Once we know this you may remember that we can use square-brackets, with
the index position of each specific character, in order to reference each
characters separately as a sub-string. (Note: the index starts at zero!)

- However, since we plan on adding the two numbers together mathematically
we must also remember to convert each character to an integer, which we
can do using the 'int()' function.
"""
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
"""
- Finally we can add the two digits together and print the output
"""
sum_of_two_digit_number = first_digit + second_digit

print(sum_of_two_digit_number)

"""
My Solution:
"""
print(int(two_digit_number[0]) + int(two_digit_number[1]))

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/705d8881-a95e-48f2-977b-840a5ec3a128?sl=47653921-6225-49e0-8a32-11ce8e710114&st=Op9u052uCErcbBL867PEnDOAQ7H5Bchq
"""
