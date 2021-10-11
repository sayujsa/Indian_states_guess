import turtle
import pandas

screen = turtle.Screen()
screen.setup(780, 897)
screen.bgpic("map.gif")
map_co = pandas.read_csv("map_coordinates.csv")
num_of_states_left = len(map_co["State"])
correct_guesses = 0

while True:
    guess = screen.textinput("States", f"Enter a state  ({correct_guesses}/{num_of_states_left})")
    if guess is None:
        break
    elif guess.title() in list(map_co["State"]):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(map_co[map_co["State"] == guess.title()]["X"]) - 20,
                    int(map_co[map_co["State"] == guess.title()]["Y"]))
        turtle.write(guess.title())
        correct_guesses += 1

    if correct_guesses == num_of_states_left:
        print("YOU WON!!, YOU HAVE GUESSED ALL 28 STATES CORRECTLY")
        break


screen.exitonclick()
