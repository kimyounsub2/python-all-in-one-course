for number in range(1, 10): # 0부터 숫자가 시작하기 때문에 9까지만 출력된다 따라서 (1 , 11)로 해줘야 10까지 출력가능
    print(number)
    
for number in range(1, 11, 3): # 3단위로 띄어서 1,4,7,10 으로 출력된다
    print(number)
    
# 1 ~ 100까지 더하기
total_number = 0
for number in range(0, 101):
    total_number += number
print(total_number)
