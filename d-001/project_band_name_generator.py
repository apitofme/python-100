"""
-=< 100 Days of Python >=-
-=[ Day 001 ]=-

Project: Band Name Generator

The goal of this project is to learn about taking input from the User,
and how to use that input as part of the output we print to the console.

By asking a couple of simple questions (e.g. "name of home town/city" and
"name of pet") we'll combine these together to suggest a Name for a Band!

Along the way we will learn a little bit about:
- Printing; Inputting; Commenting; Debugging (Name Errors & Syntax Errors);
  String Manipulation; Variables etc.

NOTE: I output the variables using an "f-string" (these have not yet been
      covered on the course) -- Official solution included below!
"""
print("Welcome to the Band Name Generator.")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print(f"Your band name could be {city} {pet}")
# OFFICIAL SOLUTION:
# print("Your band name could be " + street + " " + pet)
# -- i.e. string concatenation (using "string maths")
