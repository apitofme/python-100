"""
-=< 100 Days of Python >=-
-=[ Day 016 ]=-

Project: OOP Coffee Machine

This is an Object-Oriented reimplementation of the Coffee Machine Project
from Day 15.

NOTE: This is based on the "official solution" to the original project, with
just a couple of minor tweaks brought over from MY solution. This is largely
due to the restriction and limitations of using the provided classes. The most
notable difference/omission is how I originally handled the payment processing
component.
"""
# pylint: disable=unused-import
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects
machine = CoffeeMaker()
machine.Menu = Menu()
machine.Money = MoneyMachine()

# some tidy and prep
COMMANDS = ['report', 'off']
DRINKS = machine.Menu.get_items().rstrip('/').split('/')
# print(DRINKS)
machine.on = True
while machine.on:
    # 1. Ask for drink choice
    prompt = "\nPlease select a drink: "
    # prompt += "[E]spresso, [L]atte, [C]appuccino >> "
    prompt += ", ".join([f"[{d[0].upper()}]{d[1:]}" for d in DRINKS]) + " >> "
    ash = [d[0] for d in DRINKS]
    accepted = DRINKS + ash + COMMANDS

    valid = False
    while not valid:
        request = input(prompt).lower()
        if request not in accepted:
            print("Sorry, input not recognised.")
        else:
            valid = True

    # catch accepted shorthand (ash) inputs
    if request in ash:
        request = DRINKS[ash.index(request)]
    print(f"Request: {request}")

    # 2. Allow "OFF" command
    if request in COMMANDS:
        if request == "off":
            print("Shutting down")
            machine.on = False

        # 3. Print status report
        if request == "report":
            machine.report()
            machine.Money.report()

    else:
        # get the drink from the menu
        drink = machine.Menu.find_drink(request)
        # print(f"Drink: {drink}")

        # 4. Check enough resources
        if not machine.is_resource_sufficient(drink):
            continue

        # 5. Process payment
        # 6. Check transaction successful
        if machine.Money.make_payment(drink.cost):
            # 7. Make coffee
            machine.make_coffee(drink)
