from turtle import Screen, Turtle

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black") # 배경을 지정한다.
screen.title("My snake Game") #게임 제목을 설정
screen.tracer(0) # 애니메이션을 켜고 끌수 있다. 0 = off

starting_position = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for position in starting_position:

    new_segment= Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

# screen.update()# 실행시 모든 화면이 바로 나오게 된다. 위에서 tracer 애니메이션 동작을 껏기때문에

game_is_on = True
while game_is_on:
    screen.update()

    # 뱀의 이동할때 순차적으로 움직이기 위해
    for seg_num in range(len(segments) -1 , 0, -1): # start =2, stop = 0, step = -1
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)


screen.exitonclick()