"""
-=< 100 Days of Python >=-
-=[ Day 002 ]=-

Project: Tip Calculator
"""
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? (As Percentage: e.g. 10, 12 or 15) "))
people = int(input("How many people to split the bill? "))
pay = (bill / people) * (tip / 100 + 1)
print(f"Each person should pay: ${pay:.2f}")
