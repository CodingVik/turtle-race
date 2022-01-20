from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def press_w():
    tim.forward(10)
def press_s():
    tim.backward(10)
def press_a():
    tim.left(10)
def press_d():
    tim.right(10)
def press_c():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

#An initial dialog box pop-up to help guide the user what keys to work with for sketching.
input_text = screen.textinput(title="Instructions/Guide",
                              prompt="1.To move pointer forward, PRESS 'W'.\n"
                                     "2.To move pointer backward, PRESS 'S'.\n"
                                     "3.To revolve/turn pointer slightly to its right, PRESS 'D'.\n"
                                     "4.To revolve/turn pointer slightly to its left, PRESS 'A'.\n"
                                     "5.To clear screen and return to center, PRESS 'C'.\n\n"
                                     "Type 'Okay' to start sketching.")

#Screen listens to key strokes on keyboard.
screen.listen()
screen.onkeypress(key="w", fun=press_w)
screen.onkeypress(key="s", fun=press_s)
screen.onkeypress(key="a", fun=press_a)
screen.onkeypress(key="d", fun=press_d)
screen.onkeypress(key="c", fun=press_c)

screen.exitonclick()


