from turtle import Turtle, Screen

# Create the first turtle

stan = Turtle()
stan.shape("turtle")  # this method will change the object on the screen to turtle
stan.color('coral')
stan.forward(100)

my_screen = Screen()
my_screen.exitonclick()
