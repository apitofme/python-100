"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-

Project: Tip Calculator

The goal of today's project is to build a simple 'tip' calculator you can
use to easily calculate and add a percentage to a bill, as well as split
the bill between a given number of people, at restaurants etc.

Along the way we will learn a little about:
- Data Types; Numbers; Operations; Type Conversion; F-Strings and more!

NOTE: I used 'Presentational Formatting' in the output f-string, which is
      also used in the alternative official solution:
      - https://replit.com/@appbrewery/tip-calculator-end-alt#main.py
      Ref: https://docs.python.org/3.12/library/string.html#formatspec
"""
print("Welcome to the Tip Calculator!")
# take inputs
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? "
                  "(As Percentage: e.g. 10, 12 or 15) "))
people = int(input("How many people to split the bill? "))
# calculate amount each person has to pay including tip
pay = (bill / people) * (tip / 100 + 1)
print(f"Each person should pay: ${pay:.2f}")

"""
Note: The calculation in my solution differs from that on the course.

On the course Angela demonstrates adding the tip to the total bill
before dividing it by the number of people (which she further breaks
down in to several steps, performing each part of the calculation
separately for clarity.)

Above, my 'one-line' calculation (using BODMAS) actually splits the bill
by the number of people first, then multiplies that by the calculated
tip percentage. The result is the same either way, however my thinking
was that each person paid a __% tip, rather than the overall tip being
split between the group (just my brain working differently!).

If I wanted to I could have written it instead like this:

    pay = bill * (tip / 100 + 1) / people

Here again the bill is first multiplied by the calculated tip percentage
BEFORE being divided by the number of people! -- In hindsight I prefer this
layout of the calculation as I think it is easier to read and understand.
"""
