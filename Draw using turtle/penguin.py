import turtle

def draw_penguin():
    screen = turtle.Screen()
    screen.title("Draw a Penguin")
    t = turtle.Turtle()
    t.speed(10)

    # Draw body
    t.color("black")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Draw belly
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    # Draw eyes
    t.penup()
    t.goto(-30, 80)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    t.penup()
    t.goto(30, 80)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    # Draw beak
    t.penup()
    t.goto(0, 40)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.goto(-10, 30)
    t.goto(10, 30)
    t.goto(0, 40)
    t.end_fill()

    turtle.done()

draw_penguin()
