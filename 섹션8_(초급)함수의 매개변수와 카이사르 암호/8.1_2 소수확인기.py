#Write your code below this line 👇
#number = 7은 눌때 0이 안나옴으로 소수이다.
#  7 / 2 =
#  7 / 3 =
#  7 / 4 =
#  7 / 5 =
#  7 / 6 = 

def prime_checker(number):
    is_prime = True
    for M in range(2 ,number):
        
        if number % M == 0:
            is_prime = False
            
    if is_prime:
        print(f"{number} 값은 소수다")
    else:
        print(f"{number} 값은 소수가 아니다")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)