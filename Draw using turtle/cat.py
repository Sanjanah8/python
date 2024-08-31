import turtle

def draw_cat():
    screen = turtle.Screen()
    screen.title("Draw a Cat")
    t = turtle.Turtle()
    t.speed(10)

    # Draw head
    t.color("gray")
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    # Draw eyes
    t.penup()
    t.goto(-40, 40)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    t.penup()
    t.goto(40, 40)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    # Draw nose
    t.penup()
    t.goto(0, 20)
    t.pendown()
    t.color("pink")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Draw mouth
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.color("black")
    t.right(90)
    t.circle(10, 180)
    
    # Draw ears
    t.penup()
    t.goto(-100, 100)
    t.pendown()
    t.color("gray")
    t.begin_fill()
    t.goto(-140, 160)
    t.goto(-60, 160)
    t.goto(-100, 100)
    t.end_fill()

    t.penup()
    t.goto(100, 100)
    t.pendown()
    t.begin_fill()
    t.goto(140, 160)
    t.goto(60, 160)
    t.goto(100, 100)
    t.end_fill()

    turtle.done()

draw_cat()
