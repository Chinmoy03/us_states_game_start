import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def on_screen_click(x, y):
    print(x, y)


writer = turtle.Turtle()
writer.hideturtle()
writer.penup()
data = pandas.read_csv("50_states.csv")
screen.onscreenclick(on_screen_click)
total_guessed = 0
while True:
    input_state = screen.textinput(title="Guess State Name", prompt="Give a State Name:")
    state_row = data[data.state == input_state]
    if len(state_row) != 0:
        writer.goto(state_row.iloc[0, 1], state_row.iloc[0, 2])
        writer.write(f"{state_row.iloc[0, 0]}", align="center", font=("Arial", 8, "normal"))
        writer.home()
        total_guessed += 1
    if total_guessed == 50:
        break
    if input_state == "quit":
        writer.clear()
        for state in range(len(data)):
            # print(row)
            # writer.goto(row.x, row.y)
            # writer.write(f"{data.state}", align="center", font= ("Arial", 12, "normal"))
            writer.speed("fastest")
            row = data[data.state == state]
            writer.goto(data.iloc[state, 1], data.iloc[state, 2])
            writer.write(f"{data.iloc[state, 0]}", align="center", font= ("Arial", 8, "normal"))
        break
print(f"You were able to guess {total_guessed}/50 states.")
turtle.mainloop()


