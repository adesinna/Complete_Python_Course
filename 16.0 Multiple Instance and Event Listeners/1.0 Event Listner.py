from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
	timmy.forward(10)


def move_backward():
	timmy.backward(10)


def turn_right():
	timmy.right(10)


def turn_left():
	timmy.left(10)


def clear_turtle():
	timmy.clear()
	timmy.penup()
	timmy.home()
	timmy.pendown()


screen.listen()
screen.onkey(fun=move_forward, key='Up')  # functions do not use brackets when they are arguments
screen.onkey(fun=move_backward, key='Down')
screen.onkey(fun=turn_left, key='Left')
screen.onkey(fun=turn_right, key='Right')
screen.onkey(fun=clear_turtle, key='space')

screen.exitonclick()

