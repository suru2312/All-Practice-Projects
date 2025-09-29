import os

def ops_choice(choice):
    if choice == "espresso":
        water_consumed = 50
        coffee_consumed = 18
        check_resource(water_consumed, coffee_consumed)
        
    elif choice == "latte":
        water_consumed = 200
        coffee_consumed = 24
        milk_consumed = 150
        check_resource(water_consumed, coffee_consumed, milk_consumed)
        
    elif choice == "cappuccino":
        water_consumed = 200
        coffee_consumed = 24
        milk_consumed = 150
        check_resource(water_consumed, coffee_consumed, milk_consumed)
        
    elif choice == "report":
        for i, j in current_resource.items():
            print(i, " : ", j)
    else:
        print("Sorry Wrong Input, Try Again.")

def check_resource(water, coffee, milk = None):
    if water > current_resource["Water (ml)"]:
        return True
    else:
        return False
    if coffee > current_resource["Coffee (gm)"]:
        return True
    else:
        return False
    if milk > current_resource["Milk (ml)"]:
        return True
    else:
        return False

current_resource = {
    "Water (ml)": 1000,
    "Milk (ml)": 400,
    "Coffee (gm)": 100,
    "Money ($)": 0,
}

off = False
while not off:
    user_choice = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if user_choice == "off":
        off = True
    else:
        ops_choice(user_choice)
