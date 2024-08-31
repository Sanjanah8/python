import turtle

def draw_tree():
    screen = turtle.Screen()
    screen.title("Draw a Tree")
    t = turtle.Turtle()
    t.speed(10)

    # Draw trunk
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.left(90)
        t.forward(100)
        t.left(90)
    t.end_fill()

    # Draw leaves
    t.color("green")
    t.penup()
    t.goto(-60, -50)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    turtle.done()

draw_tree()
