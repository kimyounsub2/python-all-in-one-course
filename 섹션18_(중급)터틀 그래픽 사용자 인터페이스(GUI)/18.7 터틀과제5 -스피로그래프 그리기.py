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

youn.speed("fastest") # 터틀의 속도를 결정한다.
# youn.circle(100) # 반지름 100을 전달하는 원
# youn.color(random_color())
# current_heading = youn.heading() # 0.0을 가리킨다.

# darw_spirograph라는 새로운 함수를 생성하고 이 함수는 하나의 매개변수로 size_of_gap(간격의 크기를)받아들인다.
# 이 값은 원이 하나씩 그려지면서 각각의 원사이에 생기는 공간의 크기가 된다.
# 이 크기는 물론 터틀 화살표가 향하는 방향에 따라 결정된다.
def draw_spirograph(size_of_gap): #

    for _ in range(int(360 /size_of_gap)):
        youn.circle(100) # 반지름 100을 전달하는 원
        youn.color(random_color())
        youn.setheading(youn.heading() + size_of_gap)
    
draw_spirograph(5)
    

    
    
    
screen = Screen()
screen.exitonclick()