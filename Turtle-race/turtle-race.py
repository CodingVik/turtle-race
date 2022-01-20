from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow']
y_positions = [-80, -40, 0, 40, 80, 120]
motion = [5, 10, 15, 20]
all_turtles = []
winning_color = ""
not_end = True

for index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_positions[index])
    all_turtles.append(new_turtle)

user_bet = screen.textinput(title="Bet on your choice of turtle.",
                            prompt="Which turtle will win the race ? Enter a color: ")

while not_end:
    for turtle in all_turtles:
        turtle.forward(random.choice(motion))
        if turtle.xcor() >= 230:
            not_end = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won. {winning_color.capitalize()} turtle won the race.")
            else:
                print(f"You lost. {winning_color.capitalize()} turtle won the race.")


screen.exitonclick()