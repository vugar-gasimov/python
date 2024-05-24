import turtle
import pandas

ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

data = pandas.read_csv(r"day25\US_States_Game\50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"day25\US_States_Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_is_on = True

states = data.state.to_list()
Ohio = data[data["state"] == "Ohio"]

while game_is_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another State's name ?").title()

     # Check if answer among list of states
    if answer_state in states:
         
        new_t = turtle.Turtle()
        new_t.penup()
        new_t.hideturtle()
        new_t.write(answer_state, align=ALIGNMENT, font=FONT)
        state_in_list = data[data.state == answer_state] 
        # index_in_list = data[data[state_name].index]
    
        new_t.goto(int(state_in_list.x), int(state_in_list.y))

            





turtle.mainloop()

