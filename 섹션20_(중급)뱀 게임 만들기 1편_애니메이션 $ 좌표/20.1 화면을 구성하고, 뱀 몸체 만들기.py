from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black") # 배경을 지정한다.
screen.title("My snake Game") #게임 제목을 설정

starting_position = [(0, 0), (-20, 0), (-40, 0)]


for position in starting_position:

    new_segment= Turtle("square")
    new_segment.color("white")
    new_segment.goto(position)





screen.exitonclick()