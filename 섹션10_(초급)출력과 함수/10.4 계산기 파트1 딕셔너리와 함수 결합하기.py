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

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the Second number?: "))

for symbol in operation:
    print(symbol)
operation_symbol = input("Pick an operation from the Line above: ")
calculation_function = operation[operation_symbol]
answer = calculation_function(num1, num2)
        
            
print(f"{num1} {operation_symbol} {num2} = {answer}")


