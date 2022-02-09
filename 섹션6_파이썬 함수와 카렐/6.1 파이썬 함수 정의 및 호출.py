

print("Hello")
num_char = len("Hello")
print(num_char)

# def 함수를 생성하거나 정의한다는 의미
def my_function():
    print("Hello")
    print("Bye")
my_function()


# for문과 while 비교

# for 반복문의 경우 어떤 것을 반복하고 반복하는(fruits , 1~6) 각 아이템에 대해 뭔가를 해야 할때 유용하다
fruits = ["Apple", "Pear", "Orange"]
for fruit in fruits:
    print(fruit)
    
for n in range(1, 6):
    print(n)
    
# while 반복문의 경우 전체 순서에서 몇번째에 해당하는지 어떤 아이템을 반복할지가 아닌(for문) 그저 특정 작업을 
# 설정한 조건에 도달할 때까지 수없이 반복 수행하고자 할 때 사용
    