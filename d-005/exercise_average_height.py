"""
-=< 100 Days of Python >=-
-=[ Day 005 ]=-

Coding Exercise: Average Height (L.52)
"""
"""
Slide 1: Task
- Write a program that calculates the average height from a List of heights

Notes:
    - The average is obtained by adding all the heights together then
    dividing by the number of heights given.
    - Do NOT use the 'sum()' or 'len()' functions, instead try to replicate
    their functionality using what we've learnt about 'for' loops.
    - The average height should be rounded to the nearest whole number.

The setup for this exercise will format the input in to a list of integer
values (the heights).
"""
# Example input 1: "156 178 165 171 187"
# Example input 2: "151 145 179"
student_heights = input().split()
"""
NOTE -- Pylint suggests refactoring the exercise' code from this:

    for n in range(0, len(student_heights)):
        student_heights[n] = int(student_heights[n])

To use 'enumerate()' instead, like this:

    # have to add var 'h' because enumerate produces a 'tuple'
    for n,h in enumerate(student_heights):
        student_heights[n] = int(student_heights[n])

However it is simpler in this case to use 'map()' to apply the 'int()'
function directly to each item in the List as follows:
"""
student_heights = map(int, student_heights)

"""
Slide 2: Solution
"""
# setup counters
num_of_students = 0
total_height = 0
# loop through the list
for height in student_heights:
    # increment the count
    num_of_students += 1
    # add the height to running total
    total_height += height
# calculate the average height (and round it)
average_height = round(total_height / num_of_students)
# print the output
print(f"total height = {total_height}")
print(f"number of students = {num_of_students}")
print(f"average height = {average_height}")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/4a109ef8-ac17-4a51-85b1-61a61a20bb66?sl=9f11a807-0fb7-4665-b939-db4e73addf51&st=mNE31MHkIOQ6aD7idTqayqxc4JmqYIyT
"""
