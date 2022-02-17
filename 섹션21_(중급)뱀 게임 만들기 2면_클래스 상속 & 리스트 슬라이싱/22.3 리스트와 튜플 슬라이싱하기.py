from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black") # 배경을 지정한다.
screen.title("My snake Game") #게임 제목을 설정
screen.tracer(0) # 애니메이션을 켜고 끌수 있다. 0 = off

snake = Snake()
food = Food()
scoreboard = Scoreboard()

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
    
    
# 먹이와의 충돌 감지
# 터틀클래스의 distance 메소드를 사용하며 먹이를 먹었는지 알아낼 수있다.
# 뱀이 머리부터 먹이까지의 거리이다.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
# 벽과의 충돌 감지
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on =False
        scoreboard.game_over()
        
# 꼬리와의 충돌 감지
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
# 머리가 꼬리의 아무 세그먼트와 충돌하면 게임이 끝난것이므로 게임종료 절차진행



screen.exitonclick()