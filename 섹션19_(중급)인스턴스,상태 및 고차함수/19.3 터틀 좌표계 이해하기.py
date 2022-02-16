from turtle import Turtle, Screen
import turtle
import random
youn =Turtle()

screen = Screen()
screen.setup(width = 500, height = 400) # 표시되는 창의 폭과 높이를 설정할수 있다. 폭 =500 , 높이 400
# 팝업창을 띄워 사용자가 메시지와 제목을 읽고 텍스트를 입력하게 해준다.
user_bet = screen.textinput(title = "Make tour bet", prompt = "which turtle will win the race? Enter a color: ") 
# 사용자가 숫자를 입력하기를 원한다면 numinput 메소드를 사용할수있다.
colors = ["red" , "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]

youn = Turtle(shape="turtle")  # youn.shape("turtle") 아래칸에 이렇게 입력해도 거북이가 나오지만 더쉽게하는 방법
youn.penup() # 이동시 팬이 그려지는걸 막는다.
for turtle_index in range(0, 6):
    youn = Turtle(shape="turtle")  
    youn.penup() # 이동시 팬이 그려지는걸 막는다.
    # X값과 Y값을 정의 하여 터틀을 맨 왼쪽으로 정의한다. 
    # x가 가로 y 세로 x가 500 이니 맨 중앙 0부터 -250을 해줘야 한다. 하지만 맨끝값을 입력하면 화면에서 사라진다.
    youn.goto(x = -230, y = y_positions[turtle_index] )
    youn.color(colors[turtle_index])





screen.exitonclick()
