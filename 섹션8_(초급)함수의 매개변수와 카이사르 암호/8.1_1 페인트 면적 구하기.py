#Write your code below this line 👇
import math # 소수자리가 입력되어도 올림이 된다
def paint_calc(height, width, cover):
    area = height * width
    #  math.ceil 소숫점 올림처리하기 위해 맨위(import math) 선언해주었다
    num_of_cans = math.ceil(area / cover)    # 정수가 되었다
    print(f"You'll need {num_of_cans} cans of paint ")
#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


