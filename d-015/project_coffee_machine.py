"""
-=< 100 Days of Python >=-
-=[ Day 015 ]=-
"""
"""
NOTE: This marks the start of the ""Intermediate" section of the course!
"""
"""
Project: Coffee Machine

For our project today, imagine your company has asked you to program the code
needed to operate a coffee vending-machine. We don't have to worry about the
hardware, or actually building the machine of course, however if we look up a
real coffee vending-machine online we can get an idea of their basic features.

e.g.
1.  "Makes 3 hot flavours" -- Espresso; Latte; and Cappuccino
    - Each of these 'recipes' requires different amounts of ingredients to make,
    they also each have a different price.
    - The machine also starts with a finite amount of "resources", i.e. Water,
    Milk and (of course) Coffee.
2.  "Coin Operated" -- In U.S. currency there are 4 different coins. These are:
    - Penny, Nickel, Dime, and Quarter (NOTE: They no longer mint Dollar coins)

With these concepts established we can start to outline what our program needs
to be able to do, and list these as our program requirements:

1.  Print a report
    - We need our machine to be able to tell us how much of each resource it
    has left.
2.  Check resources are sufficient
    - In other words, make sure that there is enough water/milk etc. to make
    whatever drink a person orders, reporting back if not.
3.  Process coins
    - It needs to be able to process coins, adding their values to make sure
    it covers the cost of the drink, and returning any change due.
4.  Check transaction successful
    - If a person didn't insert enough coins for the drink they ordered then
    it should not make the drink, it should give feedback on the transaction,
    and return their money.
    - Otherwise, if the money was enough then it should go ahead and make the
    drink...
5.  Make coffee
    - The machine will need to keep track of the resources it uses as it makes
    each drink, deducting the appropriate amount from the totals for each.

Now that we have the outline for the program we can start to add more details,
working out what functionality we need in order to fulfil each requirement.
Where functionality overlaps, or is tied in to each other, and we can start to
break each 'function' up in to smaller, more manageable tasks.

>> A more detailed "Program Specification" is provided for you in the PDF file
included in this folder.

>> The starting code (included below) provides the data structures and details
for each drink on the menu, as well as the machine's starting resources.
"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
