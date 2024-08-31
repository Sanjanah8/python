import turtle

def draw_fractal(turtle_obj, length, depth):
    if depth == 0:
        turtle_obj.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            draw_fractal(turtle_obj, length / 3, depth - 1)
            turtle_obj.left(angle)

screen = turtle.Screen()
screen.bgcolor("white")
fractal = turtle.Turtle()
fractal.speed(0)

fractal.penup()
fractal.goto(-200, 100)
fractal.pendown()
draw_fractal(fractal, 400, 4)

turtle.done()
