import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data["state"]
all_states = states.to_list()
correctly_guessed_states = []

while len(correctly_guessed_states) < 50:

    user_answer = screen.textinput(title=f"{len(correctly_guessed_states)}/50", prompt="Guess a state").title()

    if user_answer in all_states:
        t1 = turtle.Turtle()
        t1.hideturtle()
        t1.penup()
        x = data[data.state == user_answer].x
        y = data[data.state == user_answer].y
        t1.goto(int(x), int(y))
        t1.write(f"{user_answer}", move=False)
        correctly_guessed_states.append(user_answer)

    if user_answer == "End":
        missing_states = []
        for state in all_states:
            if state not in correctly_guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
