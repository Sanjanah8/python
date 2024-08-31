import turtle

def draw_smiley():
    screen = turtle.Screen()
    screen.title("Draw a Smiley Face")
    t = turtle.Turtle()
    t.speed(10)

    # Draw face
    t.color("yellow")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Draw eyes
    t.penup()
    t.goto(-35, 35)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(35, 35)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    # Draw mouth
    t.penup()
    t.goto(-40, -20)
    t.pendown()
    t.color("black")
    t.right(90)
    t.circle(40, 180)

    turtle.done()

draw_smiley()
