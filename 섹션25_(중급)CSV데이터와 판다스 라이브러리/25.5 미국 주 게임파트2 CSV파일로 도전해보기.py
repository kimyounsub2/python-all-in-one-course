import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_state = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's another state's name?").title(0)

    # Alabama
    if answer_state in all_state:
        guessed_states.append(answer_state)
        youn = turtle.Turtle()
        youn.hideturtle()
        youn.penup()
        state_data = data[data.state == answer_state]
        youn.goto(int(state_data.x), int(state_data.y))
        #youn.write(answer_state)
        youn.write(state_data.state.item())

screen.exitonclick() # 클릭하면 종료된다.

# 만일 answer_state가 50_states.csv안에 있는지 체크할수 있다

