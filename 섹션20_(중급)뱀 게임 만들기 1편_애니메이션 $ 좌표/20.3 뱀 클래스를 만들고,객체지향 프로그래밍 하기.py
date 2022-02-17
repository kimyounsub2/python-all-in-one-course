from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black") # 배경을 지정한다.
screen.title("My snake Game") #게임 제목을 설정
screen.tracer(0) # 애니메이션을 켜고 끌수 있다. 0 = off

snake = Snake()

screen.listen() # 키 입력시 필요함
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()