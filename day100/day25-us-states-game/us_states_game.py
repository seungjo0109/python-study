import turtle
from numpy import result_type
import pandas

states_data = pandas.read_csv("data/us-states-game-start/50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./data/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_list = []
score = 0

while len(answer_list) <= 50:

    answer_state = screen.textinput(title=f"{score}/50 Guess the State", prompt="What's another state's name?").lower()     # you can use .title()

    if answer_state == "exit":
        break

    if states_data[states_data["state"].str.lower() == answer_state].empty:
        print("It is wrong answer")
    else:
        if answer_state not in answer_list:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()

            [x, y] = [states_data[states_data["state"].str.lower() == answer_state].x , states_data[states_data["state"].str.lower() == answer_state].y]
            t.goto(int(x), int(y))
            t.write(answer_state)

            answer_list.append(answer_state)
            score = len(answer_list)
            print(answer_list)

result_data = {
    "Answer list": answer_list,
}

data_frame = pandas.DataFrame(result_data)
data_frame.to_csv("./data/us-states-game-start/result.csv")


# turtle.mainloop()
# screen.exitonclick()