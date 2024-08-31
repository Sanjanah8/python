import turtle

def draw_fish():
    screen = turtle.Screen()
    screen.title("Draw a Fish")
    t = turtle.Turtle()
    t.speed(10)

    # Draw body
    t.color("blue")
    t.begin_fill()
    t.circle(100, 180)
    t.left(90)
    t.forward(200)
    t.left(90)
    t.circle(100, 180)
    t.end_fill()

    # Draw tail
    t.penup()
    t.goto(-100, 0)
    t.pendown()
    t.color("blue")
    t.begin_fill()
    t.goto(-150, -50)
    t.goto(-150, 50)
    t.goto(-100, 0)
    t.end_fill()

    turtle.done()

draw_fish()
