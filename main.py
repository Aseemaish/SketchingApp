import turtle
from turtle import Turtle, Screen

aseem = Turtle()
screen = Screen()


def move_forward():
    """On pressing 'w'. Moves the turtle forward by 10 units."""
    aseem.forward(10)


def move_backward():
    """On pressing 's'. Moves the turtle backward by 10 units."""
    aseem.backward(10)


def turn_left():
    """On pressing 'a'. Turns the turtle to the left by 10 degrees."""
    new_heading = aseem.heading() + 10
    aseem.setheading(new_heading)


def turn_right():
    """On pressing 'd'. Turns the turtle to the right by 10 degrees."""
    new_heading = aseem.heading() - 10
    aseem.setheading(new_heading)


def change_color_red():
    """On pressing 'r'. Changes the color of the turtle to Red"""
    aseem.color("red")


def change_color_green():
    """On pressing 'g'. Changes the color of the turtle to Green"""
    aseem.color("green")


def change_color_blue():
    """On pressing 'b'. Changes the color of the turtle to Blue"""
    aseem.color("blue")


def clear_screen():
    """Clears the screen and resets the turtle to the center."""
    aseem.clear()
    aseem.penup()
    aseem.home()
    aseem.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="r", fun=change_color_red)
screen.onkey(key="g", fun=change_color_green)
screen.onkey(key="b", fun=change_color_blue)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
