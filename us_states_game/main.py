import turtle
import pandas
from states import States

screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
states = States()

num_states = 50
num_guessed_states = 0
guessed_states = []
data = pandas.read_csv('50_states.csv')

while num_guessed_states < 50:
    answer = screen.textinput(title=f'{num_guessed_states}/{num_states} States Correct',
                              prompt="What's another state name?").title()

    if answer in data.state.to_list() and answer not in guessed_states:
        state = data.loc[data['state'] == answer, 'state'].values[0]
        x = data.loc[data['state'] == answer, 'x'].values[0]
        y = data.loc[data['state'] == answer, 'y'].values[0]
        pos = (x, y)
        states.populate_map(position=pos, state=state)
        num_guessed_states += 1
        guessed_states.append(state)

turtle.mainloop()
