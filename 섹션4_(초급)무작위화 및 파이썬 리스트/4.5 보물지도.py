from tkinter import HORIZONTAL
from turtle import position


row1 = ["π±","π±","π±"] 
row2 = ["π±","π±","π±"]
row3 = ["π±","π±","π±"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0]) #2 μλ ₯μκ° κ°λ‘ λλ²μ§Έ μΈλ‘ 3λ²μ¬λ‘ 23μ μλ ₯ν΄μ£ΌκΈ° λλ¬Έμ μ μ μ μΈκ³Ό 0μΌλ‘ μ²«λ²μ§Έ 1λ‘ λλ²μ¬
vertical = int(position[1]) #3

#μμ 1
selected_row = map[vertical -1]
selected_row[horizonal -1] = "X"
#μμ 2
map[vertical-1][horizonal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")