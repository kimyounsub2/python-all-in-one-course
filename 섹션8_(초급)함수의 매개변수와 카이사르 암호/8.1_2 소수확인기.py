#Write your code below this line π
#number = 7μ λλ 0μ΄ μλμ΄μΌλ‘ μμμ΄λ€.
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
        print(f"{number} κ°μ μμλ€")
    else:
        print(f"{number} κ°μ μμκ° μλλ€")


#Write your code above this line π
    
#Do NOT change any of the code belowπ
n = int(input("Check this number: "))
prime_checker(number=n)