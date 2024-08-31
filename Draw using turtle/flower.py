import turtle

def draw_flower():
    screen = turtle.Screen()
    screen.title("Draw a Flower")
    t = turtle.Turtle()
    t.speed(10)

    # Draw petals
    t.color("red")
    for _ in range(6):
        t.begin_fill()
        t.circle(50, 60)
        t.left(120)
        t.circle(50, 60)
        t.left(120)
        t.left(60)
        t.end_fill()

    # Draw center of the flower
    t.penup()
    t.goto(0, -20)
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    turtle.done()

draw_flower()
