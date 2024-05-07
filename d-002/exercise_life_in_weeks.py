"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-

Coding Exercise: Life in Weeks (L.25)
"""
"""
Slide 1: Task
- Create a program that calculates how many weeks we have left
to live (assuming we will live to be 90).

The input will be a person's current age, and the output should
be a message in the following format: "You have x weeks left."
"""
age = input()

"""
Slide 2: Solution
"""
# First take the current age from the total (assumed) years
years_left = 90 - int(age)
# Then convert that number of years in to weeks
weeks_left = years_left * 52
# Finally, print the output using an f-string
print(f"You have {weeks_left} weeks left.")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/70ce34ac-2968-4f2d-a523-964c824f7892?sl=42bdaa61-096d-4f32-8f1c-371f681345f6&st=voOVSS863JuNoRgjspfGFZBADWEmqWar
"""
