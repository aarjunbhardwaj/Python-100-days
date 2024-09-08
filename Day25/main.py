import turtle
import pandas

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S State Games")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

t = turtle.Turtle()
t.hideturtle()
t.penup()

guessed_states = []
state_list = data.state.to_list()

while len(guessed_states)<50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",prompt="Name a State").title()

    if answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in state_list:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in state_list:
        if answer not in guessed_states:
            guessed_states.append(answer)
            check_answer = data[data.state == answer]
            x_axis,y_axis = int(check_answer.x),int(check_answer.y)
            t.goto(x_axis,y_axis)
            t.write(f"{answer}")