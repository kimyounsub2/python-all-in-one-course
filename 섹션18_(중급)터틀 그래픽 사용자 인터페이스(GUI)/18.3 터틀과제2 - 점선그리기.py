import turtle as Y

from turtle import Screen

youn = Y.Turtle()

for _ in range(15):
    youn.forward(10)
    youn.penup()
    youn.forward(10)
    youn.pendown()

screen = Screen()
screen.exitonclick()