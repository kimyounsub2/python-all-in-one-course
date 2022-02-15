
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# 이 클래스를 이용해 객체를 만드는 것부터 시작하자
# 객체의 이름은 무엇이든 원하는 이름으로 정할수 있다.(money_machine)
# 파이썬의 기본 표기법인 스네이크 케이스를 사용해 새 변수(money_machine)을 만들고 여기에 객체를 저장
# 이 객체는 물론 MoneyMachine클래스를 이용해서 만든다
# ()를 붙여야 객체가 만들어진다.
# 이제 객체를 만들고 변수 money_machine에 저장했다.
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

# money_machine이 보고서를 만들게 하려면 객체로 들어가 점을 입력하고 필요한 메소드를 호출한다.
# money_machine.report()
# coffee_maker.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
