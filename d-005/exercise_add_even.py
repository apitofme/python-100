"""
-=< 100 Days of Python >=-
-=[ Day 005 ]=-

Coding Exercise: Adding Even Numbers (L.55)
"""
"""
Slide 1: Task
- Write a program that adds all of the EVEN numbers from 1 to 'x'
(where 'x' is any given number -- e.g. 100)

NOTE: to limit code-execution time 'x' should not exceed "1000"!
"""
target = int(input())  # Enter a number between 0 and 1000

"""
Slide 2: Solution
"""
# create a running total (accumulator)
total = 0
# loop through the generated range in 'step' increments of 2...
for n in range(0, target+1, 2):
    # ...to add just the EVEN numbers to the total
    total += n
# print out the total
print(total)

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/c8a70cc6-7b64-42ad-880b-e2034e8cb8bc?sl=6ca26e31-59e7-48b8-bd61-29aa4578dee3&st=dxa8zt7S8lJSxMK4Sf9f2ajskeJOrcsk
"""
