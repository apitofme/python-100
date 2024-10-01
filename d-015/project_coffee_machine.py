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

##
# Coffee Machine Program Requirements:
##
# 1. Prompt the user by asking:
#   “What would you like? (espresso/latte/cappuccino):”
#   a. Check the user’s input to decide what to do next.
#   b. The prompt should show every time action has completed
#   -- i.e. once the drink is dispensed, the prompt should show again to serve
#   the next customer.

# 2. Turn off the Coffee Machine by entering “off” to the prompt.
#   a. For maintainers of the coffee machine, they can use “off” as the secret
#   word to turn off the machine. Your code should end execution when this
#   happens.

# 3. Print report.
#   a. When the user enters “report” to the prompt, a report should be
#   generated that shows the current resource values, e.g:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5

# 4. Check resources sufficient?
#   a. When the user chooses a drink, the program should check if there are
#   enough resources to make that drink -- e.g. if Latte requires 200ml water
#   but there is only 100ml left in the machine. It should not continue to
#   make the drink but print: “Sorry there is not enough water.”
#   b. The same should happen if another resource is depleted
#   -- e.g. milk or coffee.

# 5. Process coins.
#   a. If there are sufficient resources to make the drink selected, then the
#   program should prompt the user to insert coins.
#   b. Remembering:
#   quarters = $0.25, dimes = $0.10, nickels = $0.05, pennies = $0.01
#   c. Calculate the monetary value of the coins inserted, e.g:
#   -- 1 quarter, 2 dimes, 1 nickel, 2 pennies = ...
#   ...0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# 6. Check transaction successful?
#   a. Check that the user has inserted enough money to purchase the drink
#   they selected -- e.g Latte cost $2.50, but they only inserted $0.52 then
#   after counting the coins the program should say:
#   “Sorry that's not enough money. Money refunded.”
#   b. But if the user has inserted enough money, then the cost of the drink
#   gets added to the machine as the profit and this will be reflected the
#   next time “report” is triggered. e.g:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#   c. If the user inserted too much money, the machine should offer change.
#   -- e.g. “Here is $2.45 dollars in change.”
#   -- The change should be rounded to 2 decimal places

# 7. Make Coffee.
#   a. If the transaction is successful and there are enough resources to make
#   the drink the user selected, then the ingredients to make the drink should
#   be deducted from the coffee machine resources, e.g:
#   -- Report before purchasing latte:
#       Water: 300ml
#       Milk: 200ml
#       Coffee: 100g
#       Money: $0
#   -- Report after purchasing latte:
#       Water: 100ml
#       Milk: 50ml
#       Coffee: 76g
#       Money: $2.5
#   b. Once all resources have been deducted, tell the user:
#   “Here is your latte. Enjoy!” -- If latte was their choice of drink.
