MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 200,
            "coffee": 24
        },
        "cost": 3.0,
    }
}

resource = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = {
    "value": 0,
}

def report():
    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")
    print(f"Money: ${money['value']}")

def check_resources(choice):
    enough = True
    if MENU[choice]['ingredients']['water'] > resource['water']:
        print(f"There isn't enough water for a {choice}.")
        enough = False
    if MENU[choice]['ingredients']['coffee'] > resource['coffee']:
        print(f"There isn't enough coffee for a {choice}.")
        enough = False
    if 'milk' in MENU[choice]['ingredients']:
        if MENU[choice]['ingredients']['milk'] > resource['milk']:
            print(f"There isn't enough milk for a {choice}.")
            enough = False
    return enough

def process_coins(quaters, dimes, nickles, pennies):
    quaters *= 0.25
    dimes *= 0.10
    nickles *= 0.05
    pennies *= 0.01
    total = quaters + dimes + nickles + pennies
    return total

def deduct_resources(choice):
    resource['water'] -= MENU[choice]['ingredients']['water']
    resource['coffee'] -= MENU[choice]['ingredients']['coffee']
    if 'milk' in MENU[choice]['ingredients']:
        resource['milk'] -= MENU[choice]['ingredients']['milk']

def coffee_machine():
    on = True
    while on:
        choice = input("What do you like? Type 'espresso', 'latte', 'cappuccino': ")
        if choice == 'report':
            report()
        elif choice == 'off':
            print("Turning Off")
            on = False
        elif check_resources(choice):
            print("Please Insert coins")
            quaters = int(input("How many Quarters?: "))
            dimes = int(input("How many Dimes?: "))
            nickles = int(input("How many Nickles?: "))
            pennies = int(input("How many Pennies?: "))
            if process_coins(quaters, dimes, nickles, pennies) == MENU[choice]['cost']:
                deduct_resources(choice)
                money['value'] += MENU[choice]['cost']
                print(f'Here is your {choice}. Have a good one!')
            elif process_coins(quaters, dimes, nickles, pennies) > MENU[choice]['cost']:
                deduct_resources(choice)
                money['value'] += MENU[choice]['cost']
                change = process_coins(quaters, dimes, nickles, pennies) - MENU[choice]['cost']
                change = round(change, 2)
                print(f"Here is ${change} in Change")
                print(f"Here is your {choice}. Have a Good One.")
            else:
                print(f"Not enough money ${process_coins(quaters, dimes, nickles, pennies)} refunded.")
        coffee_machine()

coffee_machine()