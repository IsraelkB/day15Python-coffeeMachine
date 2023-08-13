TURN_OFF = 0
REPORT = 1
MAKE_DRINK = 2
INVALID_INPUT = -10

machine_resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

drink_resources = {
    "espresso": {"water": 50, "coffee": 18, "price": 1.5},
    "latte": {"water": 200, "coffee": 24, "milk": 150, "price": 2.5},
    "cappuccino": {"water": 250, "coffee": 24, "milk": 100, "price": 3}
}

dime_currency = 0.1
penny_currency = 0.01
nickel_currency = 0.05
quarter_currency = 0.25


def print_resources():
    water = f"Water: {machine_resources['water']}ml\n"
    milk = f"Milk: {machine_resources['milk']}ml\n"
    coffe = f"Coffee: {machine_resources['coffee']}g\n"
    money = f"Money: ${machine_resources['money']}"
    return water + milk + coffe + money


def check_order(order_type):
    """the method get the input order and analyze the input"""
    if order_type == "off":
        return TURN_OFF

    elif order_type == "report":
        print(print_resources())
        return REPORT

    for drink in drink_resources:
        if order_type == drink:
            return MAKE_DRINK

    return INVALID_INPUT


def check_resources(curr_order, curr_machine_resources):
    """"this method get the order and check if there is enough resources in the coffe machine"""
    drink_order = drink_resources[curr_order]
    if drink_order["water"] > curr_machine_resources["water"] or drink_order["coffee"] > curr_machine_resources["coffee"]:
        return False
    elif curr_order != "espresso" and drink_order["milk"] > machine_resources["milk"]:
        return False
    return True


def payment_calculator(price):
    print("please insert coins.")
    quarter_currency_amount = float(input("how many quarters?:"))
    quarter_currency_amount *= quarter_currency
    dime_currency_amount = float(input("how many dimes?:"))
    dime_currency_amount *= dime_currency
    nickel_currency_amount = float(input("how many nickels?:"))
    nickel_currency_amount *= nickel_currency
    penny_currency_amount = float(input("how many pennies?:"))
    penny_currency_amount *= penny_currency

    payment = quarter_currency_amount + nickel_currency_amount + penny_currency_amount + dime_currency_amount

    excess = price - payment
    excess *= (-1)

    if excess < 0:
        return INVALID_INPUT
    return round(excess, 2)


def machine_on():
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    order_valid = check_order(order)

    if order_valid == TURN_OFF:
        return

    elif order_valid == INVALID_INPUT:
        print("The machine coffe can only make espresso/latte/cappuccino, your request is invalid!")

    elif order_valid == MAKE_DRINK:
        valid_resources = check_resources(order, machine_resources)
        order_price = drink_resources[order]["price"]
        if valid_resources:
            order_excess = payment_calculator(order_price)
            if order_excess != INVALID_INPUT:
                print(f"Here is ${order_excess} in change.")
                print(f"Here is your {order} ☕️.Enjoy!")
            else:
                print(f"Sorry that's not enough money. Money refunded.")

    machine_on()


machine_on()