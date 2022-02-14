from importlib.resources import is_resource


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 300,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 900,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# 커피양을 비교하는 합수
def is_resource_sufficient(order_ingredients):
    """주문이 가능하면 참을 반환하고 재료가 부족하면 거짓을 반환한다."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

# 동전을 계산하기 위한 함수
def process_coins():
    """투입된 동전들을 계산하여 총 금액을 계산하여 반환한다. Returns the total calculated from coins inserted."""
    print("please issert coins. ")
    total = int(input("100원짜리 몇개 ?: ")) *100
    total += int(input("10원짜리 몇개?: ")) * 10
    total += int(input("500원짜리 몇개? : "))*500
    total += int(input("50원짜리 몇개?: ")) * 50
    return total    
        
# 사용자가 입력한 동전과 커피가격을 계산해주는 함수
def is_transaction_successful(money_received, drink_cost):
    """사용자가 정상적으로 지불했을 때 참을 반환하고 지불이 부족하면 거짓을 반환한다."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)#반올림할 소숫점 2번재 자리
        print(f"Here is {change}원 in change. ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False # 함수의 마지막은 항상 return이 되어야 한다 
    # 만약 return 명령어가 print보다 앞에 있으면 print 구문의 출력 명령은 절대 실행되지 않는다.

# 계산이 완료되고 커피가 완성되면 남은 재료의 양을 계산해주는 함수
def make_coffee(drink_name, order_ingredients):# 음료의 이름을 알아야 하고 주문받은 음료의 재료도 알아야한다.
    """자판기에 잇는 재료에서 필요한 재료의 양을 차감한다."""
    for coffee in order_ingredients:
        resources[coffee] -= order_ingredients[coffee]
    print(f"Here is your {drink_name} 입니다.")
    
        
is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/capuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
                
                
    
        
        
        
        

        

