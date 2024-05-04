"""
-=< 100 Days of Python >=-
-=[ Day 003 ]=-

Coding Exercise: Pizza Order (L.36)
"""
"""
Slide 1: Task - Build an automatic pizza order program

Based on a customer's order, work out their final bill.
The criteria are:
    - Small pizza (S):      $15
    - Medium pizza (M):     $20
    - Large pizza (L):      $25
Then:
    - Add pepperoni for small pizza (Y or N):               +$2
    - Add pepperoni for medium or large pizza (Y or N):     +$3
    - Add extra cheese for any size pizza (Y or N):         +$1
"""
print("Thank you for choosing Python Pizza Deliveries!")
size = input()  # What size pizza do you want? S, M, or L
add_pepperoni = input()  # Do you want pepperoni? Y or N
extra_cheese = input()  # Do you want extra cheese? Y or N

"""
Slide 2: Solution

In the prescribed solution Angela handles the pizza sizes first with one
conditional statement group using "if...elif...else" for the three size
options. She then handle's "added pepperoni" with a separate statement,
using a nested conditional to handle the size of pizza for that. Then one
final statement to handle "extra cheese"
"""
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

"""
My solution:
"""
# Create a variable to store the bill amount, and set it zero.
bill = 0

# Then start by checking for / handling a 'Small' pizza
if size == 'S':
    bill += 15
    # ...handle optional pepperoni
    if add_pepperoni == 'Y':
        bill += 2
# (not "S") So handle a 'Medium' pizza
elif size == 'M':
    bill += 20
    # ...handle optional pepperoni
    if add_pepperoni == 'Y':
        bill += 3
# (not "S" or "M") So must be a 'Large' pizza
else:
    bill += 25
    # ...handle optional pepperoni
    if add_pepperoni == 'Y':
        bill += 3

# Handle "extra cheese" as a separate statement because it's not
# dependent on the size of pizza, it's the same price regardless!
if extra_cheese == 'Y':
    bill += 1

# Finally we print the total bill:
print(f"Your final bill is: ${bill}.")

"""
My Alternative Solution
- Match (case) statements were introduced in Python 3.10
Ref: https://docs.python.org/3/tutorial/controlflow.html#match-statements
"""
bill = 0

match size:
    case 'S':
        bill += 15
        if add_pepperoni == 'Y':
            bill += 2
    case 'M':
        bill += 20
        if add_pepperoni == 'Y':
            bill += 3
    case 'L':
        bill += 25
        if add_pepperoni == 'Y':
            bill += 3

# We still use an 'if' for the "extra cheese"
if extra_cheese == 'Y':
    bill += 1

print(f"Your final bill is: ${bill}")
