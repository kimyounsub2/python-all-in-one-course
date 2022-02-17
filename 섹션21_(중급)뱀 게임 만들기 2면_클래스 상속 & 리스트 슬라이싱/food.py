from turtle import Turtle
import random

# 상위 클래스인 Turtle를 상속 받았기 때문에 클래스안에서 사용가능하다.
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
        
    # 먹이를 새로운 위치에다 랜덤으로 뿌린다.
    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x,random_y)
        