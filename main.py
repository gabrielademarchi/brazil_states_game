import turtle
import pandas as pd
from names import StateName

screen = turtle.Screen()
screen.title("Brazil States Games")
screen.colormode(255)
image = "brazil.gif"
screen.addshape(image)
turtle.shape(image)


df = pd.read_csv("26_states.csv")
all_states = df.states.to_list()

guessed_states = []


while len(guessed_states) < 26:
    answer_state = screen.textinput(
        "Guess the State", "What's another state's name?").title()

    if answer_state == "Exit":
        # missed = set(all_states).symmetric_difference(guessed_states)
        missed = [state for state in all_states if state not in guessed_states]
        states_to_learn = pd.DataFrame(missed, columns=['Missed States'])
        states_to_learn.to_csv('states_to_learn.csv', index=True)
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = StateName()
        state_data = df[df.states == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=("Calibri", 12, "bold"))
        # t.write(state_data.states.item())
