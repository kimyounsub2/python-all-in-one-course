from turtle import Screen, Turtle

# timmy_the_turtle이라는 객체는 Turtle 클래스에서 생성된다.
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle") # Turtle그래픽에 거북이 이미지가 출력된다
timmy_the_turtle.color("red") # Turtle그래픽에 거북이 색상이 빨간색으로 출력된다
timmy_the_turtle.forward(100) # 100의 속도로 앞으로 움직인다.


screen = Screen()
screen.exitonclick() # exitonclick은 Turtle그래픽이 안사라지게 유지해주는 함수