import turtle

def draw_rocket():
    screen = turtle.Screen()
    screen.title("Draw a Rocket")
    t = turtle.Turtle()
    t.speed(10)

    # Draw rocket body
    t.color("red")
    t.begin_fill()
    t.goto(-50, -100)
    t.goto(50, -100)
    t.goto(0, 100)
    t.goto(-50, -100)
    t.end_fill()

    # Draw rocket nose
    t.color("gray")
    t.begin_fill()
    t.goto(-50, -100)
    t.goto(-20, -150)
    t.goto(-20, -100)
    t.end_fill()

    t.color("gray")
    t.begin_fill()
    t.goto(50, -100)
    t.goto(20, -150)
    t.goto(20, -100)
    t.end_fill()

    # Draw rocket flames
    t.penup()
    t.goto(-30, -100)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.goto(-40, -150)
    t.goto(-20, -150)
    t.goto(-30, -100)
    t.end_fill()

    t.penup()
    t.goto(30, -100)
    t.pendown()
    t.begin_fill()
    t.goto(40, -150)
    t.goto(20, -150)
    t.goto(30, -100)
    t.end_fill()

    turtle.done()

draw_rocket()
