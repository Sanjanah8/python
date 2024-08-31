import turtle

def draw_star(turtle_obj, size):
    for _ in range(5):
        turtle_obj.forward(size)
        turtle_obj.right(144)

screen = turtle.Screen()
screen.bgcolor("lightblue")
star = turtle.Turtle()
star.color("yellow")
star.pensize(2)

draw_star(star, 100)

turtle.done()
