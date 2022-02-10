import random
import my_module

random_integer = random.randint(1, 10) # 1 ~ 10의 중간 랜덤 숫자가 나온다
print(random_integer)

radom_float = random.random() * 5 # 0.00000000 ~ 0.99999999 의 랜덤 숫자가 나온다
print(radom_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")


print(my_module.pi) # my_module 파일의 pi = 3.14159 값을 불러 올수 있다