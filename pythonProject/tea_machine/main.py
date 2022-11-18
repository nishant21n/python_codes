MENU = {
    "a": {
        "ingredients": {
            "milk": 100,
            "tea_powder": 15,
        },
        "cost": 10,
    },
    "b": {
        "ingredients": {
            "ginger": 10,
            "milk": 110,
            "tea_powder": 20,
        },
        "cost": 15,
    },
    "c": {
        "ingredients": {
            "ginger_lemongrass": 10,
            "milk": 121,
            "tea_powder": 21,
        },
        "cost": 21,
    }
}
profit = 0
resources = {
    "ginger": 100,
    "milk": 210,
    "ginger_lemongrass": 100,
    "tea_powder": 170,
}

logo = '''
      )
     (
      )
  _.-~(~-.
 (@\`---'/.   
('  `._.'  `)
 `-..___..-' Welcome to iNNK.Tea_Vending_m/c\n🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰🔰'''


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


def process_coins(cost):
    print(f"Please insert coins of ₹{cost}.")
    total = int(input("How many ₹1 coins: "))*1
    total += int(input("How many ₹2 coins: "))*2
    total += int(input("How many ₹5 coins: "))*5
    total += int(input("How many ₹10 coins: "))*10
    print("\n")
    return total


def is_transaction_successful(money_received, tea_cost):
    if money_received >= tea_cost:
        change = money_received - tea_cost
        print(f"Here is ₹{change} in change")
        global profit
        profit += tea_cost
        return True


def make_tea(tea_name, order_ingradiants):
    for item in order_ingradiants:
        resources[item] -= order_ingradiants[item]
    teas = {"a": "ClassicTea", "b": "GingerTea", "c": "Ginger Lemongrass Tea", }
    print(f"Here is your {teas[tea_name]} ☕\n")



is_on = True

while is_on:
    print(logo)
    choice = input("What wold you like?(ClassicTea ₹10 :'A'"
                   "GingerTea ₹15: 'B' / Ginger Lemongrass Tea ₹ 21: 'C' : ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Ginger Powder : {resources['ginger']}")
        print(f"Milk : {resources['milk']}")
        print(f"Ginger Lemongrass Powder : {resources['ginger_lemongrass']}")
        print(f"Ginger Powder : {resources['ginger']}")
        print(f"Rupees : ₹{profit}")
    else:
        tea = MENU[choice]
        if is_resource_sufficient(tea["ingredients"]):
            payment = process_coins(tea["cost"])
            if is_transaction_successful(payment, tea["cost"]):
                make_tea(choice, tea["ingredients"])



