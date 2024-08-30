from menu import Menu, MenuItem
from coffee_maker import CoffeMaker
from money_machine import MoneyMachine

espresso = MenuItem('espresso',50,0,18,0.5)
latte = MenuItem('latte',200,150,24,2.5)
cappuccino = MenuItem('cappuccino',250,100,24,3.0)

menu = Menu()

coffeemaker = CoffeMaker()

money_machine = MoneyMachine()

on = True
while on:
    choice = input(f"what would you like? choose between espresso,latte and cappuccino:")
    if choice == 'off':
        print('Have a good one!')
        on = False
    elif choice == 'report':
        coffeemaker.report()
        money_machine.report()
    else:
        coffee_choice = menu.find_drink(choice)
        if coffee_choice:
            if coffeemaker.is_resource_sufficient(espresso) and money_machine.make_payment(espresso.cost):
             coffeemaker.make_coffee(coffee_choice)


