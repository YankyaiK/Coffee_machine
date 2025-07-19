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
    "money": 0
}

def espresso():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    paid = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    receipt = (paid - MENU['espresso']['cost'])
    if paid >= MENU["espresso"]["cost"] and MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["milk"] <= resources["milk"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
        print(f"Here is ${receipt} in change.")
        resources["water"] -= 50
        resources["coffee"] -= 18
        resources["money"] += 1.5
        print("Here is your espresso ☕.Enjoy!")
    else:
        print("not enough")

def latte():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    paid = (quarters*0.25) + (dimes*0.10) + (nickles*0.05) + (pennies*0.01)
    receipt = (paid - MENU['latte']['cost'])
    if paid >= MENU["latte"]["cost"] and MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"] and MENU["latte"]["ingredients"]["coffee"] <= resources["coffee"]:
        print(f"Here is ${receipt:.2f} in change.")
        resources["water"] -= 200
        resources["milk"] -= 150
        resources["coffee"] -= 24
        resources["money"] += 2.5
        print("Here is your latte ☕.Enjoy!")
    else:
        print("not enough resources")

def cappuccino():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    paid = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    receipt = (paid - MENU['cappuccino']['cost'])
    if paid >= MENU["cappuccino"]["cost"] and MENU["cappuccino"]["ingredients"]["water"] <= resources["water"] and MENU["cappuccino"]["ingredients"]["milk"] <= resources["milk"] and MENU["cappuccino"]["ingredients"]["coffee"] <= resources["coffee"]:
        print(f"Here is ${receipt} in change.")
        resources["water"] -= 250
        resources["milk"] -= 100
        resources["coffee"] -= 24
        resources["money"] += 3.0
        print("Here is your latte ☕.Enjoy!")
    else:
        print("not enough")

def report():
    print(f"Water: {resources["water"]}ml\nmilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")

def shop():
    on = True
    while on:
        order = input("What would you like? (espresso/latte/cappuccino): ")
        if order == "espresso":
            espresso()
        elif order == "latte":
            latte()
        elif order == 'cappuccino':
            cappuccino()
        elif order == 'report':
            report()
        elif order == 'off':
            break

shop()