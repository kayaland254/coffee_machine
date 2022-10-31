MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# CONSTANTS:
ESPRESSO = MENU["espresso"]["cost"]  # 1.50
LATTE = MENU["latte"]["cost"]  # 2.50
CAPPUCCINO = MENU["cappuccino"]["cost"]  # 3.00

PENNY_VALUE = 0.01
NICKEL_VALUE = 0.05
DIME_VALUE = 0.10
QUARTER_VALUE = 0.25


# TODO: Print report of all coffee machine resources
def report():
    global ingredients_report
    ingredients_report = f"Available water: {resources['water']}ml\nAvailable milk: {resources['milk']}ml\nAvailable coffee: {resources['coffee']}g"
    print(ingredients_report)
    return ingredients_report


# TODO: PROMPT USER TO SELECT DRINK
def select_drink():
    global drink_choice
    global drink
    drink_choice = input("What would you like? (espresso/ latte/ cappuccino) Type 'report' to see report.\n").lower()

    if drink_choice == "report":
        report()
        quit()
    else:
        if drink_choice == "espresso":
            drink = ESPRESSO
        elif drink_choice == "latte":
            drink = LATTE
        else:
            drink = CAPPUCCINO
        return drink


# TODO: CHECK THAT RESOURCES ARE SUFFICIENT
def check_ingredients():
    global required_coffee, required_milk, required_water
    global available_coffee, available_milk, available_water
    required_coffee = MENU[drink_choice]["ingredients"]["coffee"]
    available_coffee = resources["coffee"]
    required_milk = MENU[drink_choice]["ingredients"]["milk"]
    available_milk = resources["milk"]
    required_water = MENU[drink_choice]["ingredients"]["water"]
    available_water = resources["water"]

    if available_coffee < required_coffee:
        print("Sorry, there's not enough coffee to make this drink.")
        exit()
    elif available_milk < required_milk:
        print("Sorry, there's not enough milk to make this drink.")
        status = "error"
        exit()
    elif available_water < required_water:
        print("Sorry, there's not enough water to make this drink.")
        exit()
    else:
        return 0


# TODO: RECEIVE AND CALCULATE AMOUNT FROM USER
def receive_payment():
    print("Please insert coins.")
    quarters = float(input("How many quarters?").lower())
    dimes = float(input("How many dimes?").lower())
    nickels = float(input("How many nickels?").lower())
    pennies = float(input("How many pennies?").lower())

    global money_paid
    money_paid = (QUARTER_VALUE * quarters) + (DIME_VALUE * dimes) + (NICKEL_VALUE * nickels) + (PENNY_VALUE * pennies)


# TODO: CHECK THAT ACCURATE AMOUNT HAS BEEN RECEIVED
def payment_checker():
    if money_paid == drink:
        print(f"Here is your {drink}, enjoy!")
    elif money_paid > drink:
        balance = round(money_paid - drink, 2)
        print(f"Here is ${balance} in change, enjoy your drink!")
    else:
        print("Sorry, that's not enough money. Money refunded.")


# TODO: REDUCE INGREDIENTS AFTER DRINK HAS BEEN SERVED
def reduce_ingredients():
    water = available_water - required_water
    resources["water"] = water
    coffee = available_coffee- required_coffee
    resources["coffee"] = coffee
    milk = available_milk - required_milk
    resources["milk"] = milk


# TODO: DEFINE APP
def coffee_machine():
    select_drink()
    check_ingredients()
    receive_payment()
    payment_checker()
    reduce_ingredients()


# Keep app running continuously (While loop)
yes = True

while True:
    thirsty = input("Would you like a drink? Type 'yes' or 'no'\n").lower()
    if thirsty == "yes":
        coffee_machine()
    else:
        print("Bye bye!")
        break

