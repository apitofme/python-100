"""
-=< 100 Days of Python >=-
-=[ Day 005 ]=-

Coding Exercise: High Score (L.53)
"""
"""
Slide 1: Task
- Write a program that calculates the highest score from a List of scores.

Note: You are not allowed to use the 'max()' function!

Example input:  78 65 89 86 55 91 64 89
Example output: "The highest score in the class is: 91"

The setup for this exercise will handle converting the input string in to
a List of integer numbers.
"""
student_scores = input().split()
# Refactoring the loop below to appease Pylint!
# for n in range(0, len(student_scores)):
#    student_scores[n] = int(student_scores[n])
student_scores = map(int, student_scores)
# NOTE the 'map()' function returns an "iterator" and NOT a List!

"""
Slide 2: Solution
"""
# set a tracking variable
high_score = 0
# loop through the scores
for score in student_scores:
    # compare the current score with the tracking variable
    if score > high_score:
        # if it is greater then update the tracking variable
        high_score = score
# output result
print(f"The highest score in the class is: {high_score}")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/69cffc56-5ac8-4b20-b067-b7ac13386989?sl=ab3946cf-d481-4015-a374-2f1390f31054&st=KgNgmOQAmEicKT1FZTkeepKeBVoagBBD
"""
