MENU = {
    # espresso
    "1": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    # latte
    "2": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    # cappuccino
    "3": {
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
}
profit = 0

def process_coins():
  """Returns total calculated from coins inserted"""
  print('Please insert coins\n')
  total = int(input('How many quarters?\n')) * 0.25
  total += int(input('How many dimes?\n')) * 0.10
  total += int(input('How many nickels?\n')) * 0.05
  total += int(input('How many pennies?\n')) * 0.01
  return total

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient"""
    # print(f'order_ingredients: {order_ingredients}')
    print(f'resources remaining: {resources}\n')
    for item in order_ingredients:
       # print(order_ingredients[item])
       if order_ingredients[item] >= resources[item]:
           print(f'Insufficient {item} resource. Cannot process order\n')
           # break
           # return False
           return profit
           # print(f'{order_ingredients[item]} >= {resources[item]}')
    return True

def is_transaction_successful(money_received, drink_cost):
    """Returns True is the payment is accepted, or False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is your change: ${change}\n')
        global profit
        profit += drink_cost
        print(f'Here is your beverage. Enjoy!\n')
        return True
    else:
        print(f'Not enough money to order your coffee. Your money is refunded.\n')
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        if resources[item] >= order_ingredients[item]:
            resources[item] -= order_ingredients[item]
        else:
            print('Not enough coffee resources\n')
            return

is_on = True
while is_on:
    choice = input('Type the number of the coffee you want to order\n\n1 = espresso\n2 = latte\n3 = cappuccino\n\n')
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print('The remaining resources are:\n')
        for resource in resources:
            print(resource, resources[resource])
        print(f'The total profit is ${profit}\n')
    else:
        drink = MENU[choice]
        if choice == '1':
            print('Your order is espresso')
            print(f'The ingredients and cost are:\n{drink}\n')
            if is_resource_sufficient(drink['ingredients']) == True:
                payment = process_coins()
            print(f'You made a payment of ${round(payment,2)}\n')
            print(f'drink_cost = {drink["cost"]}')
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])
        elif choice == '2':
            print('Your order is latte')
            print(f'The ingredients and cost are:\n{drink}\n')
            if is_resource_sufficient(drink['ingredients']) == True:
                payment = process_coins()
            print(f'You made a payment of ${round(payment,2)}\n')
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])
        elif choice == '3':
            print('Your order is cappuccino')
            print(f'The ingredients and cost are:\n{drink}\n')
            if is_resource_sufficient(drink['ingredients']) == True:
                payment = process_coins()
            print(f'You made a payment of ${round(payment,2)}\n')
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink['ingredients'])