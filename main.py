from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

m = Menu()
mi = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
cm = CoffeeMaker()
mm = MoneyMachine()
flag = True

while flag:
    order = input(f"What would you like? ({m.get_items()}): ")
    drink = m.find_drink(order)
    if order == "report":
        cm.report()
        mm.report()
    elif order == "off":
        flag = False
    elif m.find_drink(order):
        if cm.is_resource_sufficient(drink):
            if mm.make_payment(drink.cost):
                cm.make_coffee(drink)