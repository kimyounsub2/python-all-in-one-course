def calculate(**Kwargs):
    print(Kwargs)
    
calculate(add=3, multipy = 5)

def calculate(n, **Kwargs):
    print(Kwargs)
    
    n += Kwargs["add"] # n =2 이고 2 + 3 = 5이다
    n *= Kwargs["multipy"] # n = 5 이고 5 * 5= 25이다.
    print(n) # n = 25
    
calculate(2, add=3, multipy = 5)


