from turtle import Turtle, Screen

tony = Turtle()
screen = Screen()


def move_forward():
	tony.forward(10)

# Event listener, listens to a key on a keyboard and trigger the function


screen.listen()
screen.onkey(fun=move_forward, key='space') # functions do not use brackets when they are arguments

screen.exitonclick()