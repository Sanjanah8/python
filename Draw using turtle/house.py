import turtle

def draw_house():
    screen = turtle.Screen()
    screen.title("Draw a House")
    t = turtle.Turtle()
    t.speed(10)

    # Draw base of the house
    t.color("yellow")
    t.begin_fill()
    for _ in range(4):
        t.forward(100)
        t.right(90)
    t.end_fill()

    # Draw roof
    t.color("brown")
    t.begin_fill()
    t.right(45)
    t.forward(70)
    t.right(90)
    t.forward(70)
    t.right(135)
    t.forward(100)
    t.end_fill()

    # Draw door
    t.penup()
    t.goto(30, -100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(40)
        t.right(90)
        t.forward(60)
        t.right(90)
    t.end_fill()

    turtle.done()

draw_house()
