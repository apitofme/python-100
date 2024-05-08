"""
-=< 100 Days of Python >=-
-=[ Day 004 ]=-

Coding Exercise: Virtual Coin Toss (L.43)
"""
"""
Slide 1: Task
- Write a program that will randomly tell the user "Heads" or "Tails"

Generate a random number (either 0 or 1) then use that number to print
out "Heads" or "Tails" -- e.g. 1 means "Heads"; 0 means "Tails"
"""
# Hint: Remember to import the random module first
import random  # nopep8

"""
Slide 2: Solution
"""
coin_toss = random.randint(0, 1)
if coin_toss == 1:
    print("Heads")
else:
    print("Tails")

"""
Ref:
https://app.auditorium.ai/lesson/eelyNMYJKXeNJAbjssSEQz0m88XvnhX6/23bb0d44-f578-4661-990b-6df00e5da175?sl=45ff3b29-326e-40e1-8303-3d1982fe0663&st=iNKsrSJ35wpkIPAt4Z9nmXB3H6jmChOs
"""
