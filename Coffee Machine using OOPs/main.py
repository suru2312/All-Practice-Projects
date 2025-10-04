# main.py
import os
import time
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# ASCII logo
logo = r"""
_________         _____  _____                  _____                .__    .__               
\_   ___ \  _____/ ____\/ ____\____   ____     /     \ _____    ____ |  |__ |__| ____   ____  
/    \  \/ /  _ \   __\\   __\/ __ \_/ __ \   /  \ /  \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\     \___(  <_> )  |   |  | \  ___/\  ___/  /    Y    \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \______  /\____/|__|   |__|  \___  >\___  > \____|__  (____  /\___  >___|  /__|___|  /\___  >
        \/                        \/     \/          \/     \/     \/     \/        \/     \/ 
"""

# Function to clear the screen and show logo
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)


money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True
cups_sold = 0  # Track total cups sold

# Start program
while is_on:
    clear_screen()
    options = menu.get_items()
    choice = input(f"What would you like? ({options}) : ").lower()
    
    if choice == "off":
        clear_screen()
        print("Turning off the Coffee Machine...")
        print("\nFinal Report:")
        coffee_maker.report()
        money_machine.report()
        print(f"Cups Sold: {cups_sold}")
        is_on = False

    elif choice == "report":
        clear_screen()
        print("Machine Report:\n")
        coffee_maker.report()
        money_machine.report()
        print(f"Cups Sold: {cups_sold}")
        input("\nPress Enter to continue...")

    else:
        drink = menu.find_drink(choice)
        if drink:
            clear_screen()
            print(f"The {drink.name} costs ${drink.cost}")
            
            # Check if resources are sufficient
            if coffee_maker.is_resource_sufficient(drink):
                # Process coins
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
                    cups_sold += 1
                    time.sleep(1)
        else:
            print("Invalid choice. Please try again.")
            time.sleep(1)
