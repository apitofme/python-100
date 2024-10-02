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

# ---------------------------- >>
# >> Solution below this line: >>
# ---------------------------- >>
import sys  # nopep8
from decimal import Decimal  # nopep8
# Ref: https://docs.python.org/3.12/library/decimal.html

##
# Globals:
# - Constants:
DEBUG_ENABLED = False
DECIMAL_FORMAT = Decimal(10) ** -2
COMMANDS = ['report', 'OFF']
DRINKS = list(MENU.keys())
COINS = {
    'quarters': Decimal(0.25),
    'dimes': Decimal(0.10),
    'nickels': Decimal(0.05),
    'pennies': Decimal(0.01)
}

# - Variables:
# dbg = []
resources['money'] = Decimal(0.00)

##
# Functions:


def ezdbg(dbg_object, dbg_message="", fnc_name=None):
    """Easily print objects and messages for debugging"""
    # Global disable debugging
    if not DEBUG_ENABLED:
        return
    header = "[Debug]: "
    if fnc_name:
        header += f"FNC:{fnc_name} -->>"

    print(f"\n{header}")

    if not dbg_message:
        if isinstance(dbg_object, list):
            try:
                for obj, msg in dbg_object:
                    # print("-- Recursion")
                    # ezdbg(obj, msg, True)
                    print(f'- {msg} "{obj}" -- {type(obj)}')
            except ValueError:
                # fallback
                print("-- Fallback")
                for item in dbg_object:
                    print(f"- {item} -- {type(dbg_object)}")
        else:
            print(f'- "{dbg_object}" -- {type(dbg_object)}')
    else:
        print(f'- {dbg_message} {dbg_object} -- {type(dbg_object)}')
    print()  # blank line


def decimal_round(x, fp=DECIMAL_FORMAT):
    """Rounds a number to a fixed number of decimal places
    Returns a Decimal (to `fp` decimal places)"""
    return Decimal(x).quantize(fp)


def decimal_multiplication(x, y, fp=DECIMAL_FORMAT):
    """Maintains fixed-point numerical format for multiplication operations
    Returns a Decimal (to `fp` decimal places)"""
    return (x * y).quantize(fp)


def decimal_division(x, y, fp=DECIMAL_FORMAT):
    """Maintains fixed-point numerical format for division operations
    Returns a Decimal (to `fp` decimal places)"""
    return (x / y).quantize(fp)
    # NOTE:
    # Addition and Subtraction with Decimals automatically preserve fixed point


def is_maintenance_operation(command):
    """Checks if the given `command` is a maintenance operation;
    Returns True/False [Boolean]"""
    return command in COMMANDS


def get_user_input(prompt, accepted):
    """Prompts the user for input using the given `prompt`;
    Validates their input against the given `accepted` [List];
    Returns the unmodified input [String]"""
    dbg = []
    dbg.append([accepted, "Accepted:"])

    input_is_valid = False
    while not input_is_valid:
        user_input = input(f"{prompt}")

        # Secretly check if the input is a valid maintenance command
        if is_maintenance_operation(user_input):
            return user_input

        # Otherwise validate as regular input (i.e. a drink)
        if user_input.lower() in accepted:
            input_is_valid = True
        else:
            print("Sorry, input not recognised. Please try again.")

    ezdbg(dbg, fnc_name="get_user_input")
    return user_input.lower()


def get_numeric_input(prompt):
    """Prompts the user for a (+ve) numeric input using the given `prompt`;
    Returns the unmodified input [String]"""
    input_is_valid = False
    while not input_is_valid:
        user_input = input(f"{prompt}")
        if user_input.isnumeric() and int(user_input) > 0:
            # NOTE: this validation ensures the number is ALSO positive!
            input_is_valid = True
        else:
            print("Invalid amount, please try again")
    return user_input


def enough_resources(requested_drink):
    """Checks there are sufficient resources to make the `requested_drink`;
    Returns True/False [Boolean]"""
    dbg = []
    dbg.append([requested_drink, "Drink:"])

    required_ingredients = MENU[requested_drink]['ingredients']
    dbg.append([required_ingredients, "Ingredients:"])
    ezdbg(dbg, fnc_name="enough_resources")

    has_sufficient = True
    for ingredient, required_amount in required_ingredients.items():
        # reset debug for loop
        dbg = []
        dbg.append([ingredient, "Ingredient:"])
        dbg.append([required_amount, "Amount Req.:"])
        dbg.append([resources[ingredient], "Amount Cur.:"])
        ezdbg(dbg, fnc_name="enough_resources")
        if resources[ingredient] < required_amount:
            print(f"Sorry there is not enough {ingredient}.")
            has_sufficient = False

    # ezdbg(dbg, fnc_name="enough_resources")
    return has_sufficient


def generate_input_prompt_options(options):
    """Generate options for an input prompt from a list of Strings;
    - i.e. capitalise first letter and wrap it in square-brackets, appending
    the rest of the word after;
    Separates the list with commas, pre-pending the last item with "or";
    Returns a String"""
    dbg = []
    dbg.append([options, "Given options:"])
    prompt = ""
    for i, opt in enumerate(options, 1):
        if i == len(options):
            prompt += "or "
        prompt += f"[{opt[0].upper()}]{opt[1:]}"
        if i != len(options):
            prompt += ", "
        if i == len(options):
            prompt += "? "
    dbg.append([prompt, "Generated prompt:"])
    ezdbg(dbg, fnc_name="generate_input_prompt_options")
    return prompt


def take_coin_input(coin, value):
    """Takes a numerical input from the user (the number of coins given);
    Returns the total value of those coins [Decimal]"""
    number_of_coins = int(get_numeric_input(f"How many {coin}? "))
    amount_given = decimal_multiplication(value, number_of_coins)
    return amount_given


def take_payment(cost):
    """Prompts a user to input coins until the required total is met;
    Asks user which coin they want to add, uses `take_coin_input`;
    Returns the total value of the coins given [Decimal]"""
    dbg = []
    total_value = Decimal(0)
    coin_names = list(COINS.keys())
    shorthands = [c[0] for c in coin_names] + ['c']

    dbg.append([f"{coin_names}", "Coin names:"])
    dbg.append([f"{shorthands}", "Shorthands:"])

    # generate the input prompt for coin selection
    prompt = "\nSelect a coin to add: "
    options = generate_input_prompt_options(coin_names + ['cancel'])
    # generate the list of accepted input values
    accepted_values = coin_names + ['cancel'] + shorthands

    # show debug before loop
    ezdbg(dbg, fnc_name="take_payment")

    while total_value < cost:
        # reset debug in loop
        dbg = []
        # current_coin = get_user_input(prompt + options, accepted_values)
        user_input = get_user_input(prompt + options, accepted_values)

        # handle 'cancel'
        if user_input in ['cancel', 'c']:
            print("Transaction cancelled.")
            break

        # handle 'shorthand' input options
        if user_input in shorthands:
            current_coin = coin_names[shorthands.index(user_input)]
        else:
            current_coin = user_input

        dbg.append([current_coin, "Selected coin:"])
        coin_total = take_coin_input(current_coin, COINS[current_coin])
        dbg.append([coin_total, "Amount given:"])

        # update the running total
        total_value += coin_total

        # check if there is still money left to pay
        if total_value < cost:
            dbg.append([total_value, "Total: $"])
            print(f"Current Total: ${total_value:.2f}")
            remaining_balance = cost - total_value
            print(f"Remaining Balance: ${remaining_balance:.2f}")
            dbg.append([remaining_balance, "Remaining: $"])
        else:
            print(f"Total paid: ${total_value}. Thank you!\n")
        # show debug in loop
        ezdbg(dbg, fnc_name="take_payment")
    return decimal_round(total_value)


def make_drink(drink):
    """Makes the drink given, deducting the quantity of ingredients used
    from the machine's resources;
    Returns the updated resources [Dictionary]"""
    dbg = []
    drink_ingredients = MENU[drink]['ingredients']
    dbg.append([drink_ingredients, "Required:"])

    # store a local copy of the global resources to modify, and return
    # - avoids use of 'global' keyword!
    updated_resources = resources
    for ingredient, quantity_used in drink_ingredients.items():
        updated_resources[ingredient] -= quantity_used

    dbg.append([resources, "Resources:"])
    dbg.append([updated_resources, "Updated:"])
    ezdbg(dbg, fnc_name="make_drink")

    return updated_resources


##
# Coffee Machine Program Requirements:
##
# Machine runs until it is switched OFF!
while True:
    # 1. Prompt the user by asking:
    #   “What would you like? (espresso/latte/cappuccino):”
    #   a. Check the user’s input to decide what to do next.
    #   b. The prompt should show every time action has completed
    #   -- i.e. once the drink is dispensed, the prompt should show again to
    #   serve the next customer.
    # ezdbg(DRINKS + COMMANDS, "ALL accepted inputs:")
    input_prompt = "Please select a drink: "
    input_options = generate_input_prompt_options(DRINKS)
    input_prompt += input_options
    accepted_shorthands = [d[0] for d in DRINKS]
    accepted_inputs = DRINKS + accepted_shorthands
    user_selection = get_user_input(input_prompt, accepted_inputs)
    print()  # blank line
    # ezdbg(f"{user_selection}", "Before:")
    if user_selection in accepted_shorthands:
        user_selection = DRINKS[accepted_shorthands.index(user_selection)]
    # ezdbg(f"{user_selection}", "After:")

    # Check for maintenance commands:
    # - i.e. handle non-drink requests
    if user_selection in COMMANDS:
        selected_operation = user_selection

        # 2. Turn off the Coffee Machine by entering “off” to the prompt.
        #   a. For maintainers of the coffee machine, they can use “off” as the
        #   secret word to turn off the machine. Your code should end execution
        #   when this happens.
        if selected_operation == "OFF":
            # Shutdown the coffee machine!
            print("Shutting down for maintenance...")
            sys.exit()

        # 3. Print report.
        #   a. When the user enters “report” to the prompt, a report should be
        #   generated that shows the current resource values, e.g:
        #       Water: 100ml
        #       Milk: 50ml
        #       Coffee: 76g
        #       Money: $2.5
        if selected_operation == 'report':
            print("Reporting current status...")
            print(f"Water: {resources['water']}ml")
            print(f"Milk:  {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']:.2f}\n")

    # Handle drinks requests:
    if user_selection in DRINKS:
        selected_drink = user_selection
        drink_cost = Decimal(MENU[selected_drink]['cost'])

        # 4. Check resources sufficient?
        #   a. When the user chooses a drink, the program should check if there
        #   are enough resources to make that drink.
        #   -- e.g. if a Latte requires 200ml water, but there is only 100ml
        #   left in the machine, it should not make the drink, but instead
        #   print: “Sorry there is not enough water.”
        #   b. The same should happen if another resource is depleted
        #   (i.e. milk or coffee).
        if not enough_resources(selected_drink):
            print("Please notify maintenance to restock the machine")
        else:
            # 5. Process coins.
            #   a. If there are sufficient resources to make the selected
            #   drink, then the program should prompt the user to insert coins.
            #   b. Remembering:
            #   quarters=$0.25, dimes=$0.10, nickels=$0.05, pennies=$0.01
            #   c. Calculate the monetary value of the coins inserted,
            #   e.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = ...
            #   ...0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
            print(f"Your {selected_drink} will cost: ${drink_cost:.2f}")
            print("Please insert coins...")
            payment_received = take_payment(drink_cost)

            # 6. Check transaction successful?
            #   a. Check that the user has inserted enough money to purchase
            #   the drink they selected -- e.g Latte cost $2.50, but they only
            #   inserted $0.52 then after counting the coins the program should
            #   say: “Sorry that's not enough money. Money refunded.”
            if payment_received < drink_cost:
                print(f"Refunding coins: ${payment_received:.2f}")
            else:
                #   b. But if the user has inserted enough money, then the cost
                #   of the drink gets added to the machine as the profit and
                #   this will be reflected the next time “report” is triggered.
                #   e.g:
                #       Water: 100ml
                #       Milk: 50ml
                #       Coffee: 76g
                #       Money: $2.5
                ezdbg(resources['money'], "Resource: $")
                resources['money'] += drink_cost
                #   c. If the user inserted too much money, the machine should
                #   offer change, e.g. “Here is $2.45 dollars in change.”
                #   The change should be rounded to 2 decimal places.
                if payment_received > drink_cost:
                    change = payment_received - drink_cost
                    print(f"You have ${change:.2f} in change.\n")
                # 7. Make Coffee.
                #   a. If the transaction is successful and there are enough
                #   resources to make the drink the user selected, then the
                #   ingredients to make the drink should be deducted from the
                #   coffee machine resources, e.g:
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
                #   b. Once all resources have been deducted, prompt the user:
                #   e.g. “Here is your latte. Enjoy!” (If they chose a latte)
                # Make the drink, updating the machine's resources
                print("Dispensing beverage...")
                resources = make_drink(selected_drink)
                print(f"Here is your {selected_drink.capitalize()}. Enjoy!\n")

    # Debugging output:
    # if dbg:
    #    ezdbg(dbg)

# NOTE: Suggested Improvements
# 1. Add a 'restock' function (to increase resources once depleted)
# 2. Handle money correctly, i.e.:
#   - Keep track of coins, both already in the machine and those entered whilst
#    giving payment.
#   - Only give change when there are the correct amount of the required coins
#   available. Print a message if unable to give exact change.
