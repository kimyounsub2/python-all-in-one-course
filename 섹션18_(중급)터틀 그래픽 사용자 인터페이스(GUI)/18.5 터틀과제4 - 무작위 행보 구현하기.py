import turtle as Y
import random

from turtle import Screen

youn = Y.Turtle()

colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# 이 리스트는 터틀이 향할 수 있는 네가지 방향을 모두 포함한다.
directions = [0, 90, 180, 270] # 동쪽은 0, 북쪽은 90, 서쪽 180, 남쪽 270
youn.pensize(10) # 터틀의 팬 사이즈를 결정한다.
youn.speed("fastest") # 터틀의 속도를 결정한다.
for _ in range(200):
    youn.forward(30)
    youn.setheading(random.choice(directions)) # setheading을 호출하고 directions의 4가지를 랜덤으로 호출할수 있다
    youn.color(random.choice(colors))
    
    
screen = Screen()
screen.exitonclick()