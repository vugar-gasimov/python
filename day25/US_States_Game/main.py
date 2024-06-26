import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S States Game")
image = r"day25\US_States_Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv(r"day25\US_States_Game\50_states.csv")

s_list = data.state.to_list()

guessed_s = []

while len(guessed_s) < 50:
    answer_state = screen.textinput(title=f"Guess States ({len(guessed_s)}/{50})", prompt="What's another state's name?").title()

    if answer_state == "Exit":
        not_guessed_s = [state for state in s_list if state not in guessed_s]
        # not_guessed_s = []
        # for state in s_list:
        #     if state not in guessed_s:
        #         not_guessed_s.append(state)
        new_data = pd.DataFrame(not_guessed_s)
        new_data.to_csv(r"day25\US_States_Game\not_guessed_states.csv")
        break
    # If answer_state is one of the states in all the states of the 50_states.csv
        # If they got it right:
        
    if answer_state in s_list:
        
        guessed_s.append(answer_state)
        new_t = turtle.Turtle()
        new_t.hideturtle()
        new_t.penup()
        s_data = data[data.state == answer_state]
        new_t.goto(int(s_data.x), int(s_data.y))
        # Create a turtle to write the name of the state at the state's x and y coordinate.
        new_t.write(answer_state)
        # new_t.write(s_data.state)
        # new_t.write(s_data.state.item())
        
        
# with open(fr"day25\US_States_Game\not_guessed_states.csv", mode="w") as n_list:
#     n_list.write(not_guessed_s)