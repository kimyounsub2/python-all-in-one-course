#Write your code below this line π
import math # μμμλ¦¬κ° μλ ₯λμ΄λ μ¬λ¦Όμ΄ λλ€
def paint_calc(height, width, cover):
    area = height * width
    #  math.ceil μμ«μ  μ¬λ¦Όμ²λ¦¬νκΈ° μν΄ λ§¨μ(import math) μ μΈν΄μ£Όμλ€
    num_of_cans = math.ceil(area / cover)    # μ μκ° λμλ€
    print(f"You'll need {num_of_cans} cans of paint ")
#Write your code above this line π
# Define a function called paint_calc() so that the code below works.   

# π¨ Don't change the code below π
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


