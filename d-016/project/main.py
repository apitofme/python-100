from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects
machine = CoffeeMaker()
machine.Menu = Menu()
machine.Money = MoneyMachine()

# some tidy and prep
COMMANDS = ['report', 'OFF']
DRINKS = machine.Menu.get_items().rstrip('/').split('/')
print(DRINKS)
machine.on = True

while machine.on:
    # 1. Ask for drink choice
    prompt = "Please select a drink: "
    prompt += "[E]spresso, [L]atte, [C]appuccino"
    ash = [d[0] for d in DRINKS]
    accepted = DRINKS + ash + COMMANDS
    valid = False
    while not valid:
        drink = input(prompt).lower()
        if drink not in accepted:
            print("Sorry, input not recognised.")
        else:
            valid = True

    # 2. Allow "OFF" command
    if drink in COMMANDS:
        if drink == "OFF":
            print("Shutting down")
            machine.on = False

        # 3. Print status report
        if drink == "report":
            machine.report()

    else:
        # 4. Check enough resources
        if not machine.is_resource_sufficient(drink):
            break

        # 5. Process payment

    # 6. Check transaction successful
    # 7. Make coffee
