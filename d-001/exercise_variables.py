"""
-=< 100 Days of Python >=-
-=[ Day 001 ]=-

Coding Exercise: Variables (L.13)
"""
"""
Slide 1: Task - Switch the values stored in 2 different variables
"""
a = input()  # 29
b = input()  # 41
# - we want to make 'a' = 41 and 'b' = 29

"""
Slide 2: Solution

In order to do this we must create a third variable to temporarily hold
one of the values while we swap the other by re-assigning it. We can then
re-assign that temporarily stored value to the opposite original variable.
"""
c = a  # (temporarily) store the value from 'a' in a new variable 'c'
a = b  # assign the value of 'b' to variable 'a' (now they're the same)
b = c  # then update variable 'b' with the stored value in 'c'

# Now, to show that the values have been switched we print 'a' and 'b'
print("a: " + a)
print("b: " + b)

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/8a8d2e46-c56a-435b-98f3-bcd71216dd26?sl=36082d05-7d6a-4879-9601-46ee008c54ba&st=SQoWtwQ9IXGxWD5znFZAcD2urRYogFfr
"""
