"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-

Project: Tip Calculator
"""
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? (As Percentage: \
    e.g. 10, 12 or 15) "))
people = int(input("How many people to split the bill? "))
pay = (bill / people) * (tip / 100 + 1)
print(f"Each person should pay: ${pay:.2f}")
"""
Note: The calculation in my solution differs from that on the course.

On the course Angela demonstrates adding the tip to the total bill
before dividing it by the number of people. (She further breaks this
down in to several steps, performing each part of the calculation
separately, for clarity.)

Above, my 'one-line' calculation (using BODMAS) actually splits the bill
by the number of people first, then multiplies that by the calculated
tip percentage. The result is the same either way, however my thinking
was that each person paid a __% tip, rather than the overall tip being
split between the group (just my brain working differently!).

If I wanted to I could have written it instead like this:

    pay = bill * (tip / 100 + 1) / people

Here the bill is (again) multiplied by the calculated tip percentage
first, then divided by the number of people. -- In hindsight I much
prefer this layout of the calculation as I think it is easier to read
and understand!
"""
