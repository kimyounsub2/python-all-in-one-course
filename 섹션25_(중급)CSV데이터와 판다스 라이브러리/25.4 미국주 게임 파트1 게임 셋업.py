import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

answer_state = screen.textinput(title = "Guess the State", prompt = "What's another state's name?")

screen.exitonclick() # 클릭하면 종료된다.

