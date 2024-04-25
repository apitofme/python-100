"""
-=< 100 Days of Python >=-
-=[ Day 001 ]=-

Coding Exercise: Input Function (L.12)
"""
# Slide 1: Introduction to Auditorium

# Slide 2: Input works differently here!
# - in order to test output correctly we omit the prompt
print(input("What is your name?")) #❌ DON'T do this
print(input()) #✅ DO this

# Slide 3: Submit and be subjected to Hidden Tests!
num1 = int(input()) #2
num2 = int(input()) #3

print(num1 * num2)

# Slide 4: Cheaters be warned, we test more than what you see!
num1 = int(input())
num2 = int(input())

print(6)

# Slide 5: Input Playground - change, run, reset and play around
# Try it yourself. Print the input text into the output area.
# (You will need to add items to the input area in order to run this)
for i in range(0,4):
    print(input())

# Slide 6: Len can count so you don't have to
# - the "len()" function will output the length of something
#   e.g. the number of characters in a string
numOfLetters = len("Henry")
print(numOfLetters)

# Slide 7: Test - calculate the number of characters in any given name

# Slide 8: Solution
print(len(input()))

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/d83e1847-3ad1-4f67-9f9f-7cbfb9dd970f?sl=451daad1-9e51-47e2-a755-543c84f04c51&st=dd7d7d89-dd35-4d61-99a7-19d44a45f61f
"""
