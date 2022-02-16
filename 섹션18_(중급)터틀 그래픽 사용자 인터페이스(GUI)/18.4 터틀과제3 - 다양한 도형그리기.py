import turtle as Y
import random

from turtle import Screen

youn = Y.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides): # 이 함수는 그리려는 도형의 변의 개수를 입력받는다.
    angle = 360 / num_sides
    for _ in range(num_sides):
        youn.forward(100)
        youn.right(angle)
        
for shape_side_n in range(3, 11):
    youn.color(random.choice(colors))
    draw_shape(shape_side_n) 
    # 따라서 shape_side_n을 draw_shape함수로 전달하여 3에서 10까지 증가하도록 한다.


screen = Screen()
screen.exitonclick()