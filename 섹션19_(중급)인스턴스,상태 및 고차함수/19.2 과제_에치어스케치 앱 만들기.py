from turtle import Turtle, Screen

youn = Turtle()
screen = Screen()

def move_forwards():
    youn.forward(10)
    
def move_backwards():
    youn.backward(10)
    
def move_right():
    youn.right(10)
    youn.forward(10)
    # new_heading = youn.heading() + 10
    # youn.setheading(new_heading)
    
def move_left():
    youn.left(10)
    youn.forward(10)
    # new_heading = youn.heading() - 10
    # youn.setheading(new_heading)
    
def clear_drawing():
    youn.reset()


screen.listen()
screen.onkey(fun = move_forwards, key = "w")
screen.onkey(fun = move_backwards, key = "s")
screen.onkey(fun = move_right, key = "d")
screen.onkey(fun = move_left, key = "a")
screen.onkey(fun = clear_drawing, key = "c")
screen.exitonclick()
