from tkinter import HORIZONTAL
from turtle import position


row1 = ["🐱","🐱","🐱"] 
row2 = ["🐱","🐱","🐱"]
row3 = ["🐱","🐱","🐱"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

horizonal = int(position[0]) #2 입력자가 가로 두번째 세로 3번재로 23을 입력해주기 때문에 정수 선언과 0으로 첫번째 1로 두번재
vertical = int(position[1]) #3

#예제1
selected_row = map[vertical -1]
selected_row[horizonal -1] = "X"
#예제2
map[vertical-1][horizonal-1] = "X"

print(f"{row1}\n{row2}\n{row3}")