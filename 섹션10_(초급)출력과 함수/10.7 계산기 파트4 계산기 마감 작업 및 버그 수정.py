from art import logo
print(logo)


# 덧셈
def add(n1, n2):
    return n1 + n2

# 뺄셈
def subtract(n1, n2):
    return n1 - n2

# 곱하기
def multiply(n1, n2):
    return n1 * n2

# 나누기
def divide(n1, n2):
    return n1 / n2

# 이 연산(operation)이라고 하는 변수 안에 4가지 계산식을 저장한다.
# 이제 아래의 딕셔너리는 4가지 계산식 함수를 호출하는 수단으로 사용된다.
operation = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}
# 작업자가 n이라고 입력해도 계산기가 종료되지 않고 다시 처음부터 시작 하는것을 프로그래밍에서는 재귀라고 한다.
# 재귀 : 기본적으로 직접 호출할 수 잇는 함수를 가질 수 있다는 개념
def calculator():
    print(logo)
    # int는 정수이기 때문에 소숫점을 가져올수 없다 float로 소수점을 변환하는 함수를 사용하면 정수인 숫자도 가져올수 있다
    num1 = float(input("What's the first number?: "))

    for symbol in operation:
        print(symbol)
    should_continu = True

    while should_continu:    
        operation_symbol = input("Pick an operation from the Line above: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operation[operation_symbol]
        answer = calculation_function(num1, num2)
                
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'Y' to continue calculating with {answer}, or type 'n' to exit.: ") == "Y":
            num1 = answer
        else:
            should_continu = False
            calculator()
calculator()
