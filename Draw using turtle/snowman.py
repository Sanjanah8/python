import turtle

def draw_snowman():
    screen = turtle.Screen()
    screen.title("Draw a Snowman")
    t = turtle.Turtle()
    t.speed(10)

    # Draw snowman body
    t.color("white")
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    t.penup()
    t.goto(0, -100)
    t.pendown()
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.begin_fill()
    t.circle(120)
    t.end_fill()

    # Draw eyes
    t.penup()
    t.goto(-15, 50)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    t.penup()
    t.goto(15, 50)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    # Draw nose
    t.penup()
    t.goto(0, 40)
    t.pendown()
    t.color("orange")
    t.begin_fill()
    t.goto(0, 30)
    t.goto(20, 30)
    t.goto(0, 40)
    t.end_fill()

    turtle.done()

draw_snowman()
