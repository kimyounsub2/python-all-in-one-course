import turtle as Y
import random

from turtle import Screen

youn = Y.Turtle()
Y.colormode(255) # RGB 색상

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color



# 이 리스트는 터틀이 향할 수 있는 네가지 방향을 모두 포함한다.
directions = [0, 90, 180, 270] # 동쪽은 0, 북쪽은 90, 서쪽 180, 남쪽 270
youn.pensize(10) # 터틀의 팬 사이즈를 결정한다.
youn.speed("fastest") # 터틀의 속도를 결정한다.
for _ in range(200):
    youn.color(random_color())
    youn.forward(30)
    youn.setheading(random.choice(directions)) # setheading을 호출하고 directions의 4가지를 랜덤으로 호출할수 있다
   
    
    
screen = Screen()
screen.exitonclick()