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
    answer_state = screen.textinput(title = f"{len(guessed_states)}/50 States Correct", prompt = "What's another state's name?").title()
    # if문을 리스트 컴프리헤션 적용시키기
    if answer_state == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_lear.csv")
        break

    # if answer_state == "Exit":
    #     missing_states = []
    #     for state in all_state:
    #         if state not in guessed_states:
    #             missing_states.append(answer_state)
    #     new_data = pandas.DataFrame(missing_states)
    #     new_data.to_csv("states_to_lear.csv")
    #     break
    if answer_state in all_state:
        guessed_states.append(answer_state)
        youn = turtle.Turtle()
        youn.hideturtle()
        youn.penup()
        state_data = data[data.state == answer_state]
        youn.goto(int(state_data.x), int(state_data.y))
        #youn.write(answer_state)
        youn.write(state_data.state.item())



# 만일 answer_state가 50_states.csv안에 있는지 체크할수 있다