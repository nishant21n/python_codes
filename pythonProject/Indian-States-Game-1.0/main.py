import turtle
import pandas

screen = turtle.Screen()
screen.title("Indian States Game")
screen.setup(width=700, height=700)
image = "India_map.gif"
screen.addshape(image)

turtle.shape(image)
# def get_mouse_click_cor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_cor)
# turtle.mainloop()

data = pandas.read_csv("Indian States.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/28 States Correct",
                                    prompt="What's another state's name?").title()

    # If answer_state is one of the states in all the states of the Indian States.csv
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Missed_states.csv")
        break

    if answer_state in answer_state:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state, font=("Arial", 6, "normal"))
        # t.write(state_data.state.item())#also possible




screen.exitonclick()
