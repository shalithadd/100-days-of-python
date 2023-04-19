import turtle
import pandas


screen = turtle.Screen()
screen.title('U.S. States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

num_states = 50
num_guessed_states = 0
guessed_states = []
data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()

while num_guessed_states < 50:
    answer = screen.textinput(title=f'{num_guessed_states}/{num_states} States Correct',
                              prompt="What's another state name?").title()

    if answer == 'Exit':
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_state_data = pandas.DataFrame(missed_states)
        missed_state_data.to_csv('states_to_learn.csv')
        break

    if answer in all_states and answer not in guessed_states:
        state_data = data[data.state == answer]
        text = turtle.Turtle()
        text.hideturtle()
        text.penup()
        text.goto(state_data.x.item(), state_data.y.item())
        text.write(answer)
        num_guessed_states += 1
        guessed_states.append(answer)

