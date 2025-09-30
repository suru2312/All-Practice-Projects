# Coffee Machine Program
import os
import time

logo = r"""
_________         _____  _____                  _____                .__    .__               
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____    ____ |  |__ |__| ____   ____  
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/                        \/     \/          \/     \/     \/     \/        \/     \/ 
"""

MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0,
    }
}

resources = {
    "water": 10000,
    "milk": 4000,
    "coffee": 1000,
    "money": 0.0,
}

cups_sold = 0  # Track total cups sold


def clear_screen():
    """Clear screen and show logo"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)


def is_resource_sufficient(order_ingredients):
    """Returns True when resources are enough, False if not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ($0.25/coin): "))
    dimes = int(input("How many dimes? ($0.10/coin): "))
    nickles = int(input("How many nickles? ($0.05/coin): "))
    pennies = int(input("How many pennies? ($0.01/coin): "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        resources["money"] += drink_cost
        return True
    else:
        print(f"Sorry that's not enough money. ${round(money_received, 2)} refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    global cups_sold
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    cups_sold += 1
    clear_screen()
    print(f"Here is your {drink_name}. Enjoy! ☕")


def report():
    """Prints the report of resources."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")
    print(f"Total Cups Sold: {cups_sold}")


def coffee_machine():
    clear_screen()
    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            clear_screen()
            print("Turning off the Coffee Machine...")
            report()  # Show final report before shutdown
            is_on = False
        elif choice == "report":
            clear_screen()
            report()
        elif choice in MENU:
            drink = MENU[choice]
            if is_resource_sufficient(drink["ingredients"]):
                # Show the cost before asking coins
                print(f"The {choice} costs ${drink['cost']}. Please insert coins.")
                payment = process_coins()
                if is_transaction_successful(payment, drink["cost"]):
                    make_coffee(choice, drink["ingredients"])
        else:
            clear_screen()
            print("Invalid choice. Please select again.")
            time.sleep(1)


# Run the coffee machine
coffee_machine()
