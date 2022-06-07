from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Object instantiation
coffee_maker_obj = CoffeeMaker()
menu_obj = Menu()
money_machine_obj = MoneyMachine()

# Coffee machine on flag
is_on = True

# 1. Print report
coffee_maker_obj.report()
money_machine_obj.report()

while is_on:
    print(f"Menu: \n {menu_obj.get_items()}")
    choice = input("What menu do you like? ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_obj.find_drink(choice)

        # 2. Check resources sufficient? 
        is_sufficient = coffee_maker_obj.is_resource_sufficient(drink)
        
        # 3. Process Coin, Check transaction successful
        is_payment = money_machine_obj.make_payment(drink.cost)

        if is_sufficient and is_payment:
            # 5. Make coffee
            coffee_maker_obj.make_coffee(drink)
        else:
            pass