def add(*args): # *args(아스테리스크 키워드)
    print(args[0]) # 0번째 숫자가 출력된다.
    
    sum = 0
    for n in args:
        sum += n
    return sum

# args를 사용하면 원하는 숫자를 입력하고 add 함수를 사용하면 어느값이든 적용하여 사용할수 있다.
print(add(3, 5, 6))
print(add(5,5,4,8,9,10,100))